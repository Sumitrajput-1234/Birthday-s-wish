# Program to store employee data and retrieve details

# Creating a list of employees (each employee is represented as a dictionary)
employees = [
    {"id": 101, "name": "Alice", "department": "HR", "salary": 50000},
    {"id": 102, "name": "Bob", "department": "IT", "salary": 60000},
    {"id": 103, "name": "Charlie", "department": "Finance", "salary": 55000},
    {"id": 104, "name": "David", "department": "Marketing", "salary": 52000}
]

# Function to retrieve employee details by ID
def get_employee_details(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            return emp
    return "Employee not found!"

# Example usage
search_id = int(input("Enter Employee ID to search: "))
details = get_employee_details(search_id)

print("\nEmployee Details:")
print(details)
