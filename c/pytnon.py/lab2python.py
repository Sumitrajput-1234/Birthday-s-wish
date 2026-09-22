print("\nPYTHON BUILT-IN SEQUENCES DEMONSTRATION\n")

print("a) CREATING SEQUENCES OF EACH TYPE\n")

my_string = "Hello Python"
print("1. String: ",my_string)

my_list = [10, 20, 30, 40, 50, 60]
print("2. List: ",my_list)

my_tuple = (100, 200, 300, 400, 500)
print("3. Tuple: ",my_tuple)

my_bytes = b"Python"
print("4. Bytes: ",my_bytes)

my_bytearray = bytearray(b"Hello")
print("5. Bytearray: ",my_bytearray)

my_range = range(5, 15, 2)
print("6. Range: range(5, 15, 2) = ",list(my_range))

print("\nb) INDEXING -\n")

print("String - Index [0]: ",my_string[0])
print("String - Index [-1]: ",my_string[-1])

print("List - Index [2]: ",my_list[2])
print("List - Index [-2]: ",my_list[-2])

print("Tuple - Index [1]: ",my_tuple[1])
print("Tuple - Index [-3]: ",my_tuple[-3])

print("Bytes - Index [0]: ",my_bytes[0])
print("Bytes - Index [3]: ",my_bytes[3])

print("Bytearray - Index [0]: ",my_bytearray[0])
print("Bytearray - Index [2]: ",my_bytearray[2])

print("Range - Index [0]: ",my_range[0])
print("Range - Index [3]: ",my_range[3])

print("\nc) SLICING -\n")

print("String [0:5]: ",my_string[0:5])
print("String [6:]: ",my_string[6:])
print("String [::2]: ",my_string[::2])

print("List [1:4]: ",my_list[1:4])
print("List [:3]: ",my_list[:3])
print("List [::2]: ",my_list[::2])

print("Tuple [1:4]: ",my_tuple[1:4])
print("Tuple [2:]: ",my_tuple[2:])
print("Tuple [::-1]: ",my_tuple[::-1])

print("Bytes [0:3]: ",my_bytes[0:3])
print("Bytes [2:]: ",my_bytes[2:])

print("Bytearray [1:4]: ",my_bytearray[1:4])
print("Bytearray [:3]: ",my_bytearray[:3])

print("Range [1:4]: ",list(my_range[1:4]))
print("Range [:3]: ",list(my_range[:3]))

print("\nd) MODIFYING MUTABLE SEQUENCES\n")

print("1. MODIFYING LIST:\n")
print("Original List: ",my_list)

my_list[0] = 99
print("After changing index [0] to 99: ",my_list)

my_list.append(70)
print("After appending 70: ",my_list)

my_list.remove(30)
print("After removing 30: ",my_list)

my_list.insert(2, 25)
print("After inserting 25 at index 2: ",my_list)

print("\n2. MODIFYING BYTEARRAY:\n")
print("Original Bytearray: ",my_bytearray)

my_bytearray[0] = 72
print("After changing index [0] to 72(H): ",my_bytearray)

my_bytearray.append(33)
print("After appending 33 (!): ",my_bytearray)

print("\ne) FINDING NUMBER OF ELEMENTS IN A LIST\n")

def count_elements(lst):
    count = 0
    for element in lst:
        count += 1
    return count

lst = [5, 10, 15, 20, 25, 30, 35]
print("Sample List: ",lst)
print("Number of elements in List: ",count_elements(lst))

print("\nf) CHECKING IF LIST IS IN ASCENDING ORDER\n")

def is_ascending(lst):
    if len(lst)<=1:
        return True
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            return False
    return True

list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 20, 15, 30, 40]
list3 = [5, 5, 5, 5]
list4 = [100]

print("List 1: ",list1)
print("Is in ascending order? ",is_ascending(list1),"\n")

print("List 2: ",list2)
print("Is in ascending order? ",is_ascending(list2),"\n")

print("List 3: ",list3)
print("Is in ascending order? ",is_ascending(list3),"\n")

print("List 4: ",list4)
print("Is in ascending order? ",is_ascending(list4),"\n")

print("\ng) DISPLAY LIST OF EVEN NUMBERS USING RANGE FUNCTION\n")

print("Using range(start, stop, step)")
even_numbers1 = range(0, 21, 2)
print("Even numbers from 0 to 20: ",list(even_numbers1))

even_numbers2 = range(2, 51, 2)
print("Even numbers from 2 to 50: ",list(even_numbers2))