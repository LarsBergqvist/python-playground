import array

# Encode items as signed short (2-byte) integers
numbers = array.array('h', [2, -1, 0, 1, 2])
view = memoryview(numbers)
print(view.obj)
print(view.tolist())

# Create a new view with showing the data as signed chars
view_bytes = view.cast('b')
# The underlying object is still showed as short ints
print(view_bytes.obj)
# But the new view shows the data as bytes
print(view_bytes.tolist())

# Change the most significant byte of the
# first signed short integer to 3 =>
# 2 + 256 + 512 = 770
view_bytes[1] = 3
# The underlying original data is affected
print(numbers)

del view
del view_bytes
