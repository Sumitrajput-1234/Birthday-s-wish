
class Person:
    # Nested class
    class Dob:
        def __init__(self, day, month, year):
            self.day = day
            self.month = month
            self.year = year

        def display_dob(self):
            print(f"DOB: {self.day}-{self.month}-{self.year}")

    def __init__(self, name, day, month, year):
        self.name = name
        # Creating object of nested class
        self.dob = Person.Dob(day, month, year)

    def display_person(self):
        print("Name:", self.name)
        self.dob.display_dob()


# Create Person object
p = Person("Rahul", 15, 8, 2000)

# Display details
p.display_person()