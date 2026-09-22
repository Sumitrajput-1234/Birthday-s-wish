# Program to find common elements in two lists

# Define two lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

# Method 1: Using set intersection
common_elements = list(set(list1) & set(list2))

print("List 1:", list1)
print("List 2:", list2)
print("Common Elements:", common_elements)