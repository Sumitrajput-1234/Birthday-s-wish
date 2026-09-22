# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages

#     # Overloading the > operator
#     def __gt__(self, other):
#         return self.pages > other.pages


# # Creating book objects
# book1 = Book("Python Basics", 350)
# book2 = Book("Data Structures", 500)

# # Comparing books using >
# if book1 > book2:
#     print(f'"{book1.title}" has more pages than "{book2.title}"')
# else:
#     print(f'"{book2.title}" has more pages than "{book1.title}"')

# Remove duplicates from a list

# my_list = [1, 2, 3, 2, 4, 1, 5]

# # Using set()
# unique_list = list(set(my_list))

# print("Original List:", my_list)
# print("List after removing duplicates:", unique_list)

# from collections import defaultdict

# # Creating a default dictionary with int as default value
# d = defaultdict(int)

# # Adding values
# d['a'] += 1
# d['b'] += 2

# print(d)
# print("Value of key 'c':", d['c'])   # returns default value 0

# from collections import OrderedDict

# # Creating Ordered Dictionary
# od = OrderedDict()

# od['apple'] = 3
# od['banana'] = 2
# od['orange'] = 5

# print("Ordered Dictionary:")
# for key, value in od.items():
#     print(key, ":", value)

# from collections import Counter

# # List of elements
# items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# # Creating Counter dictionary
# count = Counter(items)

# print("Counter Dictionary:")
# print(count)

# i = 1 
# while i<=1000:
#     print(i)
#     i =i+1 

class Parrot:
    def __init__(self, name, age):
        self.name = name      # Instance attribute
        self.age = age

parrot1 = Parrot("Blu", 10)
parrot2 = Parrot("Woo", 15)

print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")

