# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
print("1. Change x so that it is [1, 2, 3, 4], x: ")
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]

print("2. Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10], x: ")
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
print("3. Change x so that it is [1, 2, 3, 4, 9, 10], x:")
x.pop(4)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
print("Change x so that it is [1, 2, 3, 4, 9, 99, 10], x: ")
x.extend([99,100])
print(x)

# Print the length of list x
print("Print the length of list x, length:")
print(len(x))
# Print all the values in x multiplied by 1000
print("Print all the values in x multiplied by 1000, values:")

for i in range(len(x)):
    print(x[i]*1000)