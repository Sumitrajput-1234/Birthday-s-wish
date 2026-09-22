class A:
    def show(self):
        print("Show method from class A")

class B:
    def display(self):
        print("Display method from class B")

def invoke_method(obj, method_name):
    # Try to get the method dynamically
    method = getattr(obj, method_name, None)
    
    if callable(method):
        method()
    else:
        print(f"Method '{method_name}' not found in object")

# Create objects
a = A()
b = B()

# Invoke methods without knowing object type
invoke_method(a, "show")       # exists in A
invoke_method(b, "display")    # exists in B

# Call a method that does NOT exist
invoke_method(a, "display")    # not in A