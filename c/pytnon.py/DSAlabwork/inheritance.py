# Base class 1
class Father:
    def skills_father(self):
        print("Father: Gardening, Driving")

# Base class 2
class Mother:
    def skills_mother(self):
        print("Mother: Cooking, Painting")

# Derived class inheriting from both Father and Mother
class Child(Father, Mother):
    def skills_child(self):
        print("Child: Coding")

# Create object of Child class
c = Child()

# Call methods from both base classes and child class
c.skills_father()
c.skills_mother()
c.skills_child()