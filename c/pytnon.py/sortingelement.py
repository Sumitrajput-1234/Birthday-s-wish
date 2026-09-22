# Program to sort elements in a list using Bubble Sort

def bubble_sort(my_list):
    n = len(my_list)
    # Traverse through all elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return my_list

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", my_list)
sorted_list = bubble_sort(my_list)
print("Sorted list:", sorted_list)