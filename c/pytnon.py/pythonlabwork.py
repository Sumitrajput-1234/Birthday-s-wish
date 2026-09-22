# Q14: Star Patterns in Python

# # Right-angled triangle
# def right_angle_triangle(n):
#     for i in range(1, n+1):
#         print("*" * i)

# # Equilateral triangle
# def equilateral_triangle(n):
#     for i in range(1, n+1):
#         print(" " * (n-i) + "*" * (2*i-1))

# # Diamond shape
# def diamond(n):
#     # Upper half
#     for i in range(1, n+1):
#         print(" " * (n-i) + "*" * (2*i-1))
#     # Lower half
#     for i in range(n-1, 0, -1):
#         print(" " * (n-i) + "*" * (2*i-1))

# # Driver code
# size = 10
# print("Right-angled Triangle:")
# right_angle_triangle(size)

# print("\nEquilateral Triangle:")
# equilateral_triangle(size)

# print("\nDiamond Shape:")
# diamond(size)


# Q15: Sum of digits and reverse digits

# def sum_and_reverse(num):
#     # Convert number to string for easy manipulation
#     num_str = str(num)
    
#     # Sum of digits
#     digit_sum = sum(int(digit) for digit in num_str)
    
#     # Reverse digits
#     reversed_num = num_str[::-1]
    
#     return digit_sum, int(reversed_num)

# # Example usage
# number = int(input("Enter a number: "))
# digit_sum, reversed_num = sum_and_reverse(number)

# print(f"Sum of digits: {digit_sum}")
# print(f"Reversed number: {reversed_num}")

# from datetime import datetime

# # User-defined function to calculate age
# def calculate_age(dob_str):
#     # Convert DOB string to datetime object
#     dob = datetime.strptime(dob_str, "%d-%m-%Y")
    
#     # Get today's date
#     today = datetime.today()
    
#     # Calculate age in years
#     age = today.year - dob.year
    
#     # Adjust if birthday hasn't occurred yet this year
#     if (today.month, today.day) < (dob.month, dob.day):
#         age -= 1
    
#     return age

# # Example usage
# dob_input = input("Enter your Date of Birth (DD-MM-YYYY): ")
# age = calculate_age(dob_input)

# print(f"Your age is: {age} years")

# Q17: Character reading and counting

# def char_counter():
#     count_numbers = 0
#     count_upper = 0
#     count_lower = 0
#     count_negative = 0

#     print("Enter characters one by one (end with #):")
#     while True:
#         ch = input()

#         if ch == "#":
#             break
#         elif ch.isdigit():
#             # Check if it's a negative number (like -5)
#             # Since input is single char, '-' alone is not a digit
#             count_numbers += 1
#         elif ch.isupper():
#             count_upper += 1
#         elif ch.islower():
#             count_lower += 1
#         elif ch.startswith("-") and ch[1:].isdigit():
#             # Handles negative numbers if user types them fully
#             count_negative += 1

#     print("\nResults:")
#     print(f"Numbers: {count_numbers}")
#     print(f"Uppercase letters: {count_upper}")
#     print(f"Lowercase letters: {count_lower}")
#     print(f"Negative numbers: {count_negative}")

# # Run the function
# char_counter()

# Define two lists
# list1 = [20, 45, 60, 15, 80]
# list2 = [40, 10, 25, 50, 30]

# # Use map with lambda to compute element-wise sums
# sums = list(map(lambda x, y: x + y, list1, list2))

# # Filter sums greater than 50
# greater_than_50 = list(filter(lambda x: x > 50, sums))

# # Print results
# print("Element-wise sums:", sums)
# print("Sums greater than 50:", greater_than_50)

# Read a 5-digit number from user
# num = input("Enter a 5-digit number: ")

# # Convert each digit into a list of integers
# digits_list = list(map(int, num))

# print("List of digits:", digits_list)

# Define a list
# my_list = [10, 20, 30, 40, 50]

# # Reverse using slicing
# print("Reversed list:", my_list[::-1])

# # OR using reversed() function
# print("Reversed list (method 2):", list(reversed(my_list)))

# Define a list
# numbers = [12, 45, 78, 23, 56, 89, 5]

# # Use built-in functions
# max_num = max(numbers)
# min_num = min(numbers)

# print("Maximum element:", max_num)
# print("Minimum element:", min_num)

#question 6 
# Create a set
# my_set = {1, 2, 3}
# print("Initial set:", my_set)

# # Add an element
# my_set.add(4)
# print("After adding 4:", my_set)

# # Remove an element
# my_set.remove(2)
# print("After removing 2:", my_set)

# # Add multiple elements
# my_set.update([5, 6, 7])
# print("After update:", my_set)

# # Create a frozenset
# my_frozenset = frozenset([10, 20, 30])
# print("Frozenset:", my_frozenset)

# Create dictionary
# student = {"Alice": 85, "Bob": 90, "Charlie": 78}
# print("Initial dictionary:", student)

# # Access value
# print("Marks of Bob:", student["Bob"])

# # Add new key-value pair
# student["David"] = 92
# print("After adding David:", student)

# # Delete a key
# del student["Alice"]
# print("After deleting Alice:", student)


# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("number", type=int, help="Enter a number")
# args = parser.parse_args()

# print("Square:", args.number ** 2)

# import argparse

# def main():
#     # Create the parser
#     parser = argparse.ArgumentParser(description="Calculate the square of a number.")

#     # Add argument
#     parser.add_argument("number", type=float, help="The number to square")

#     # Parse arguments
#     args = parser.parse_args()

#     # Calculate square
#     result = args.number ** 2

#     # Display result
#     print(f"The square of {args.number} is {result}")

# if __name__ == "__main__":
#     main()

# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("base", type=int, help="Base number")
# parser.add_argument("power", type=int, help="Power value")
# args = parser.parse_args()

# print("Result:", args.base ** args.power)


import argparse

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Calculate power of a number.")

    # Add arguments
    parser.add_argument("base", type=float, help="Base number")
    parser.add_argument("exponent", type=float, help="Exponent value")

    # Parse arguments
    args = parser.parse_args()

    # Calculate power
    result = args.base ** args.exponent

    # Display result
    print(f"{args.base} raised to the power {args.exponent} is {result}")

if __name__ == "__main__":
    main()
