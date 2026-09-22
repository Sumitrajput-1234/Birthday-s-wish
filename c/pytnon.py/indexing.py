# 1. List
list_seq = [10, 20, 30, 40, 50]
print("List:", list_seq)
print("Element at index 2 in list:", list_seq[2])  # 30

# 2. Tuple
tuple_seq = (5, 15, 25, 35, 45)
print("\nTuple:", tuple_seq)
print("Element at index 3 in tuple:", tuple_seq[3])  # 35

# 3. Range
range_seq = range(1, 11)  # 1 to 10
print("\nRange:", list(range_seq))
print("Element at index 4 in range:", range_seq[4])  # 5

# 4. String
string_seq = "Python"
print("\nString:", string_seq)
print("Character at index 1 in string:", string_seq[1])  # y

# 5. Bytes
bytes_seq = bytes([65, 66, 67, 68])  # ASCII for A, B, C, D
print("\nBytes:", bytes_seq)
print("Element at index 2 in bytes:", bytes_seq[2])  # 67

# 6. Bytearray
bytearray_seq = bytearray([97, 98, 99, 100])  # ASCII for a, b, c, d
print("\nBytearray:", bytearray_seq)
print("Element at index 0 in bytearray:", bytearray_seq[0])  # 97