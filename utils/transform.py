def byte2uint(xbytes: bytes) -> int:
    """比特转整数"""
    return int.from_bytes(xbytes, "big")


def str_to_bin(string) -> str:
    """字符串转二进制字符串"""
    return bin(byte2uint(string.encode()))[2:]


def uint2byte(x: int) -> bytes:
    """整数转比特, 32位"""
    if x == 0:
        return bytes(1)
    return x.to_bytes((x.bit_length() + 7) // 8, "big")  # 做到尽量不补零


def bin_to_str(bin_string) -> str:
    """二进制字符串转字符串"""
    return uint2byte(int(bin_string, 2)).decode()
