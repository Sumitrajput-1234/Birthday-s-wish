# def bubble_sort(arr):
#     n = len(arr)
#     # Traverse through all elements in the list
#     for i in range(n):
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#             # Swap if the element found is greater than the next element
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

#     return arr

# # Example usage
# if __name__ == "__main__":
#     my_list = [64, 34, 25, 12, 22, 11, 90]
#     print("Original list:", my_list)
#     sorted_list = bubble_sort(my_list)
#     print("Sorted list:", sorted_list)

# lst = [1, 2, 3, 2, 4, 2, 5]
# element = int(input("Enter element to count: "))

# count = lst.count(element)
# print("Occurrences:", count)

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# common = list(set(list1) & set(list2))
# print("Common elements:", common)

# employees = [
#     {"id": 1, "name": "Amit", "salary": 50000},
#     {"id": 2, "name": "Neha", "salary": 60000},
#     {"id": 3, "name": "Raj", "salary": 55000}
# ]

# emp_id = int(input("Enter employee ID: "))

# for emp in employees:
#     if emp["id"] == emp_id:
#         print("Employee details:", emp)
#         break
# else:
#     print("Employee not found")

# A = [[1, 2, 3],
#      [4, 5, 6]]

# B = [[7, 8, 9],
#      [1, 2, 3]]

# result = [[0, 0, 0],
#           [0, 0, 0]]

# for i in range(len(A)):
#     for j in range(len(A[0])):
#         result[i][j] = A[i][j] + B[i][j]

# print("Sum matrix:")
# for row in result:
#     print(row)

# t = (10, 20, 30, 20, 40)

# element = int(input("Enter element to find: "))

# if element in t:
#     index = t.index(element)
#     print("First occurrence at index:", index)
# else:
#     print("Element not found")
# t = (10, 20, 30, 40)

# lst = list(t)

# pos = int(input("Enter position to replace: "))
# new_value = int(input("Enter new value: "))

# if 0 <= pos < len(lst):
#     lst[pos] = new_value
#     t = tuple(lst)

# print("Updated tuple:", t)

# t = (10, 20, 30, 40)

# lst = list(t)

# pos = int(input("Enter position to delete: "))

# if 0 <= pos < len(lst):
#     lst.pop(pos)
#     t = tuple(lst)

# print("Updated tuple:", t)

# d = {
#     "a": 10,
#     "b": 20,
#     "c": 30
# }

# total = sum(d.values())

# print("Sum of values:", total)

# players = {
#     "Virat": 85,
#     "Rohit": 60,
#     "Dhoni": 45,
#     "Gill": 70
# }

# name = input("Enter player name: ")

# if name in players:
#     print(name, "scored", players[name], "runs")
# else:
#     print("Player not found")

# string = input("Enter a string: ")

# freq = {}

# for ch in string:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# print("Character frequencies:", freq)

# d = {"a": 3, "c": 1, "b": 2}

# # Sort by keys
# sorted_by_keys = dict(sorted(d.items()))
# print("Sorted by keys:", sorted_by_keys)

# # Sort by values
# sorted_by_values = dict(sorted(d.items(), key=lambda item: item[1]))
# print("Sorted by values:", sorted_by_values)

# keys = ["a", "b", "c"]
# values = [1, 2, 3]

# d = dict(zip(keys, values))

# print("Dictionary:", d)

# d = {"a": 1, "b": 2, "c": 3, "d": 4}

# result = {k: v**2 for k, v in d.items() if v % 2 == 0}

# print("Filtered & squared dictionary:", result)

# class Demo:
#     def __init__(self):
#         self.public_var = "I am public"
#         self.__private_var = "I am private"

#     def show_private(self):
#         return self.__private_var

# obj = Demo()

# print(obj.public_var)          # Accessible
# print(obj.show_private())      # Access via method
# print(obj.__private_var)     # Will give error

# def add(a, b, c=0):
#     return a + b + c

# print(add(2, 3))        # Two numbers
# print(add(2, 3, 4))     # Three numbers

# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Marks:", self.marks)

# s1 = Student("Rahul", 20, 85)
# s1.display()

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def grade(self):
#         if self.marks >= 75:
#             return "A"
#         elif self.marks >= 50:
#             return "B"
#         else:
#             return "C"

#     def display(self):
#         print("Name:", self.name)
#         print("Marks:", self.marks)
#         print("Grade:", self.grade())

# # Multiple students
# students = [
#     Student("Amit", 80),
#     Student("Neha", 65),
#     Student("Ravi", 40)
# ]

# for s in students:
#     s.display()
#     print()

# Fibonacci series up to n terms

# Take input from user
# n = int(input("Enter the number of terms: "))

# # First two terms
# a, b = 0, 1

# # Check if n is valid
# if n <= 0:
#     print("Please enter a positive integer.")
# elif n == 1:
#     print("Fibonacci series up to", n, "term:")
#     print(a)
# else:
#     print("Fibonacci series:")
#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# # Sample data
# number = 123.456789
# name = "Rahul"
# salary = 50000

# # 1. Right alignment
# print("Right aligned number:")
# print(f"{number:>15}")

# # 2. Left alignment
# print("\nLeft aligned number:")
# print(f"{number:<15}")

# # 3. Up to 5 decimal positions
# print("\nNumber up to 5 decimal places:")
# print(f"{number:.5f}")

# # 4. Using f-strings (example)
# print("\nUsing f-strings:")
# print(f"The value of number is {number} and salary is {salary}")

# # 5. Display name and salary using replacement fields
# print("\nName and Salary:")
# print(f"Name: {name}, Salary: {salary}")

# Input numbers from user
binary = input("Enter a binary number: ")
octal = input("Enter an octal number: ")
hexa = input("Enter a hexadecimal number: ")

# Convert to decimal
decimal_from_binary = int(binary, 2)
decimal_from_octal = int(octal, 8)
decimal_from_hexa = int(hexa, 16)

# Display results
print("\nDecimal equivalents:")
print("Binary to Decimal:", decimal_from_binary)
print("Octal to Decimal:", decimal_from_octal)
print("Hexadecimal to Decimal:", decimal_from_hexa)