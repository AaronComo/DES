# DES

## Usage

Encrypt or decrypt a message.

~~~python
from DES.DES import DES
from keygen.KeyGenerator import KeyGenerator

des = DES()
msg = "Your text here."
key = KeyGenerator().keygen()
M = des.encrypt(msg, key)
C = des.decrypt(M, key)
~~~

You can also call `des.get_padding()` to get zero padding bits.

## Notes

Message contains Chinese characters are NOT supported due to Unicode encoding.