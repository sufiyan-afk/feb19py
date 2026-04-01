# tuple is a built in data type that lets us create immutable sequences of values

# tuple is immutable

# we cannot change values once the tuple is created

# tup = (1) this is int not tuple 
#tup = (1,) this is tuple

# slicing is possible
"""
eg.
tup = (1,2,3,4)
tup[0] = 5   not allowed
"""

tup = (2,1,3,1)
print(type(tup))

print(tup[1])

print(tup[1:4])