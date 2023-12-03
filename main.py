"""
描述: DES算法实现
组织: NCC @ WHU
作者: AaronComo
日期: 2023.12.1
"""

from DES.DES import DES
from keygen.KeyGenerator import KeyGenerator
from utils.transform import str_to_bin, bin_to_str


kegen = KeyGenerator()
des = DES()

text = "NCC2021 - AaronComo"
key = kegen.keygen()  # 获取随机密钥
M = des.encrypt(text, key)
C = des.decrypt(M, key)
padding = des.get_padding()
bin_C = str_to_bin(text)
bin_M = des.encrypt(M, key, decrypt=True)

print()
print("明文字符串:\t", text)
print("二进制明文:\t", bin_C)
print("64位密钥:\t", key)
print("Zero padding:\t {}位".format(padding))
print("加密后二进制:\t", M)
print("解密后二进制:\t", bin_M)
print("解密后字符串:\t", C)
print()
