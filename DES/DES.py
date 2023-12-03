import sys

sys.path.append(r"../")
from pprint import pprint
from keygen.KeyGenerator import KeyGenerator
from permutation.permutes import *
from utils.transform import bin_to_str, str_to_bin


class DES:
    def __init__(self):
        self.padding = 0
        self.kegen = KeyGenerator()
        self.ip = IP()
        self.ip_inv = IPInverse()
        self.E = E()
        self.S = S()
        self.P = P()

    def _f(self, R, subkey):
        extended = self.E.handle(R)  # 选择运算E, 32 -> 48
        m = self._xor(extended, subkey)  # 48位扩展分组^子密钥
        m = self.S.handle(m)
        m = self.P.handle(m)
        return m

    def _xor(self, a, b):
        """两字符串逐位异或"""
        assert len(a) == len(b)
        m = str()
        for i in range(len(a)):
            m += str(int(a[i]) ^ int(b[i]))
        return m

    def encrypt(self, text: str, key64: str, decrypt=False):
        plain_text = text if decrypt else str_to_bin(text)
        subkeys = self.kegen.get_subkeys(key64, decrypt=decrypt)

        # 对最后一组进行64位对齐
        if not decrypt:
            self.padding = (64 - len(plain_text) % 64) % 64
            plain_text += "0" * self.padding  # zero padding

        # 分组加密
        cipher = str()
        for round in range(0, len(plain_text), 64):
            L = list()
            R = list()
            # print("================ 加密开始 ================")
            M = plain_text[round : round + 64]

            # 初始变换
            m = self.ip.handle(M)
            L.append(m[:32])
            R.append(m[32:])

            # 16轮feistel, 对32位的左右结构进行加密、异或和交换
            temp = str()
            for i in range(16):
                L.append(R[i])  # L[i] = R[i-1]
                temp = self._f(R[i], subkeys[i])  # f(R[i-1], subkeys[i])
                temp = self._xor(temp, L[i])  # ↑ ^ L[i-1]
                R.append(temp)  # R[i] = ↑

            # 左右交换
            m = R[16] + L[16]

            # 逆初始变换
            m = self.ip_inv.handle(m)

            # 结果添加一个分组
            cipher += m

        return cipher

    def decrypt(self, cipher, key64):
        return bin_to_str(
            self.encrypt(cipher, key64, decrypt=True)
            [: len(cipher) - self.padding]
        )

    def get_padding(self):
        return self.padding
