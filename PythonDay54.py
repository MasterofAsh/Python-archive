# a = [1, 2, 43]
# b = [1, 2, 43]
# (a is b) is false in this case, because both data types are mutable/changeable
a = "harry"
b = "harry"
# (a is b) is true. as python stores same values in the same location

print(a is b) # checks for exact location of object in memory
print(a == b) # checks for value