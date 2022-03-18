import struct

# Read 100 bytes of a png file to a memoryview
with open('icon-72x72.png', 'rb') as fp:
    img = memoryview(fp.read(100))

# Slice the header of the png file
header = img[:8]
# Cast to unsigned char
print(header.cast('B').tolist())
print(bytes(header))

del img
del header

# Read 100 bytes of a gif file to a memoryview
with open('icon-72x72.gif', 'rb') as fp:
    img = memoryview(fp.read(100))
# Slice the header of the png file
header = img[:10]
# Cast to unsigned char
print(header.cast('B').tolist())
# Unpack bytes to tuple with format little-endian,
# a sequence of 6 bytes ('GIF + version) and two 16bit unsigned integers
# representing with and height
gif_tuple = struct.unpack('<6sHH', header)
print(gif_tuple)

del img
del header

