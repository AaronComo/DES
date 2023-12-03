import os


class KeyGenerator():
    def __init__(self):
        # 置换选择1, 相比书中每项减去1, 下标从0开始
        self.REPLACE_C = [
            56, 48, 40, 32, 24, 16,  8,
            0,  57, 49, 41, 33, 25, 17, 
            9,   1, 58, 50, 42, 34, 26, 
            18, 10,  2, 59, 51, 43, 35,
        ]

        self.REPLACE_D = [ 
            62, 54, 46, 38, 30, 22, 14,
            6,  61, 53, 45, 37, 29, 21, 
            13,  5, 60, 52, 44, 36, 28, 
            20, 12,  4, 27, 19, 11,  3,
        ]

        # 置换选择2
        self.REPLACE_2 = [
            13, 16, 10,  23, 0,  4, 
            2,  27, 14,  5, 20,  9, 
            22, 18, 11,  3, 25,  7, 
            15,  6, 26, 19, 12,  1, 
            40, 51, 30, 36, 46, 54, 
            29, 39, 50, 44, 32, 47, 
            43, 48, 38, 55, 33, 52, 
            45, 41, 49, 35, 28, 31,
        ]

        self.shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    def get_subkeys(self, key64, decrypt=False):
        """ 根据64位密钥产生16个48位子密钥 """
        # assert self.check(key64)    # 保证密钥正确
        key56 = str()
        subkeys = list()
        # 去除校验位, 将其余位数打乱重排, 前28位C0, 后28位D0
        for i in self.REPLACE_C + self.REPLACE_D:
            key56 += key64[i]
        C = key56[:28]
        D = key56[28:]

        # 产生子密钥
        for i in range(16):
            # 循环左移
            step = self.shift[i]
            C = C[step:] + C[:step]
            D = D[step:] + D[:step]

            # 置换选择2
            key48 = str()
            plain = C + D
            for j in self.REPLACE_2:
                key48 += plain[j]
            subkeys.append(key48)
        
        # 解密返回倒序子密钥
        return subkeys[::-1] if decrypt else subkeys
        
    def _xor7(self, block):
        return (
            int(block[0]) 
            ^ int(block[1]) 
            ^ int(block[2]) 
            ^ int(block[3]) 
            ^ int(block[4]) 
            ^ int(block[5]) 
            ^ int(block[6])
        )
    
    def check(self, key64):
        """ 密钥校验 """
        for i in range(0, 64, 8):
            block = key64[i : i + 8]
            checksum = self._xor7(block)
            if checksum != int(block[7]):
                return False
        return True

    def keygen(self):
        """ 生成随机密钥 """
        seed = os.urandom(8)
        key64 = str()
        for i in seed:
            s = "{:08b}".format(i)[1:]
            key64 += f"{s}{self._xor7(s)}"
        return key64
