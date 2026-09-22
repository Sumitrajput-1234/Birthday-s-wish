# class Demo:
#     def __init__(self):
#         self.public_var = "I am Public"
#         self.__private_var = "I am Private"

#     def show_private(self):
#         return self.__private_var

# obj = Demo()

# print(obj.public_var)        # Accessing public variable
# print(obj.show_private())    # Accessing private variable via method

# def add(a, b, c=0):
#     return a + b + c

# print(add(2, 3))       # Adds two numbers
# print(add(2, 3, 4))    # Adds three numbers

# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

# s1 = Student("Rahul", 20, 85)

# print(s1.name, s1.age, s1.marks)

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print("Name:", self.name, "Marks:", self.marks)

# students = [
#     Student("Aman", 80),
#     Student("Riya", 90),
#     Student("Karan", 75)
# ]

# for s in students:
#     s.display()

# class Student:
#     def set_data(self, name, marks):   # Mutator
#         self.name = name
#         self.marks = marks

#     def get_data(self):               # Accessor
#         return self.name, self.marks

# s = Student()
# s.set_data("Neha", 88)

# print(s.get_data())

# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds!")
#         else:
#             self.balance -= amount

#     def display(self):
#         print("Balance:", self.balance)

# acc = BankAccount(1000)
# acc.deposit(500)
# acc.withdraw(200)
# acc.withdraw(2000)
# acc.display()

# class Test:
#     count = 0

#     def __init__(self):
#         Test.count += 1

#     @staticmethod
#     def show_count():
#         print("Total objects created:", Test.count)

# t1 = Test()
# t2 = Test()
# t3 = Test()

# Test.show_count()

# class Emp:
#     def __init__(self):
#         self.name = "John"
#         self.salary = 50000

# class Myclass(Emp):
#     def display(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)

# obj = Myclass()
# obj.display()

class Base:
    def __init__(self):
        print("Base constructor")

    def show(self):
        print("Base method")

class Derived(Base):
    def __init__(self):
        super().__init__()   # Calling base constructor
        print("Derived constructor")

    def display(self):
        super().show()       # Calling base method
        print("Derived method")

d = Derived()
d.display()