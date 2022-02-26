#!/usr/bin/python3
from itertools import cycle

plain_message = 'This is plain text'
encryption_key = 'secret_key'

print('Plain message: ' + plain_message)
print('Plain message as bytes : ' + ''.join(str(ord(c)) for c in plain_message))

# xor encrypt. xor every byte in the message with the cyclic key
encrypted = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(plain_message, cycle(encryption_key)))
print('Encrypted message as bytes: ' + ''.join(str(ord(c)) for c in encrypted))

# xor decrypt. xor every byte of the encrypted message with the cyclic key
decrypted = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(encrypted, cycle(encryption_key)))
print('Decrypted message as bytes : ' + ''.join(str(ord(c)) for c in decrypted))
print('Decrypted message: ' + decrypted)
