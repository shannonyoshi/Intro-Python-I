"""
Python tuples are sort of like lists, except they're immutable and
are usually used to hold heterogenous data, as opposed to lists
which are typically used to hold homogenous data. Tuples use 
parens instead of square brackets. 

More specifically, tuples are faster than lists. If you're looking
to just define a constant set of values and that set of values 
never needs to be mutated, use a tuple instead of a list. 

Additionally, your code will be safer if you opt to "write-protect"
data that does not need to be changed. Tuples enforce immutability
automatically. 
"""

# Example:

import math

def dist(a, b):
    """Compute the distance between two x,y points."""
    x0, y0 = a  # Destructuring assignment
    x1, y1 = b
    
    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

a = (2, 7)   # <-- x,y coordinates stored in tuples
b = (-14, 72)

# Prints "Distance is 66.94"
print("*****Example******")
print("Distance is: {:.2f}".format(dist(a, b)))
print("******End******")


# Write a function `print_tuple` that prints all the values in a tuple

print("1. Write a function `print_tuple` that prints all the values in a tuple, output:  ")

t = (1, 2, 5, 7, 99)
def print_tuple(tuple):
    for x in tuple:
        print(x)

print_tuple(t)  # Prints 1 2 5 7 99, one per line

# Declare a tuple of 1 element then print it
print("2. Declare a tuple of 1 element then print it, output: ")
u = (1,)  # What needs to be added to make this work?

def print_tuple1(tuple):
    print(tuple)

print_tuple1(u)