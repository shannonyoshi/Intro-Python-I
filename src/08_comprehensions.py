"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""
print("1. Write a list comprehension to produce the array [1, 2, 3, 4, 5]")

y = [x+1 for x in range(5)]
# for x in range(5):
#     y.append(x+1)
print(y)

print(
    "2. Write a list comprehension to produce the cubes of the numbers 0-9:, expected output:  [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]")

y = [x**3 for x in range(10)]
# for x in range(10):
#     y.append(x*x)
print(y)


print("3. Write a list comprehension to produce the uppercase version of all the elements in array a. Hint: 'foo'.upper() is 'FOO'.")

a = ["foo", "bar", "baz"]

y = [x.upper() for x in a]
# for x in a:
#     y.append(x.upper())
print(y)


print("4. Use a list comprehension to create a list containing only the _even_ elements the user entered into list x.")


x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [num for num in x if int(num) % 2 ==0 ]
# for element in x:
#     if (int(element) % 2 == 0):
#         y.append(element)
print(y)