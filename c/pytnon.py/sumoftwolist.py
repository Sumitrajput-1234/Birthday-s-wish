# Two lists
list1 = [20, 45, 60, 10, 80]
list2 = [40, 20, 30, 50, 10]

sums = list(map(lambda x, y: x + y, list1, list2))

#sums greater than 50
result = list(filter(lambda x: x > 50, sums))

print("Sums greater than 50:", result)