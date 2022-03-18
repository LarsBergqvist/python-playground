ascii = 'hello'.encode('ascii')
print('ascii:', ascii)

latin1 = 'helloåäö'.encode('latin1')
print('latin1:', latin1)

u8 = 'hello😀'.encode('utf_8')
print('utf-8:', u8)

# UTF-16 with default endian
# Will prepend a BOM with fffe (little endian)
# or feff (big endian) to the byte array
u16 = 'hello😀'.encode('utf_16')
print('utf-16:', u16)

# force encoding with little-ending
# No BOM is prepended
u16le = 'hello😀'.encode('utf_16le')
print('utf-16le:', u16le)

# Force encoding with big-ending
# No BOM is prepended
u16be = 'hello'.encode('utf_16be')
print('utf-16be', u16be)
