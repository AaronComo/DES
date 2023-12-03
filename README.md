# DES

## Usage

Encrypt or decrypt a message using DES algorithm.

~~~python
from DES.DES import DES
from keygen.KeyGenerator import KeyGenerator

des = DES()
msg = "Your text here."
key = KeyGenerator().keygen()
C = des.encrypt(msg, key)
M = des.decrypt(C, key)
~~~

You can also call `des.get_padding()` to get zero padding bits.

## Notes

- Message contains Chinese characters are **NOT** supported due to Unicode encoding.
- This program prioritizes presenting the implementation methods in a clearer manner rather than focusing on performance.
