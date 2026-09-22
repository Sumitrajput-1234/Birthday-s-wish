# Program to count occurrences of each element in a list

my_list = [1, 2, 2, 3, 4, 4, 4, 5]

# Using a dictionary to store counts
occurrences = {}
for item in my_list:
    occurrences[item] = occurrences.get(item, 0) + 1

print("Occurrences of each element:")
for key, value in occurrences.items():
    print(f"{key}: {value}")