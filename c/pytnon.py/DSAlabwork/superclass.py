# Superclass
class Animal:
    def __init__(self):
        print("Animal constructor called")

    def sound(self):
        print("Animal makes a sound")

# Subclass
class Dog(Animal):
    def __init__(self):
        # Overriding constructor
        print("Dog constructor called")

    def sound(self):
        # Overriding method
        print("Dog barks")

# Create object of subclass
d = Dog()

# Call overridden method
d.sound()