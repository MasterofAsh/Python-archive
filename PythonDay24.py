tup = (2, 4, 7, 69, 420, 25, 32, 77)
print(type(tup), tup)

# Tuples do not support changing after they have been created, this means that no new
# values can be assigned to tuples after their original values

if 2 in tup:
    print("Yes")
else:
    print("No")

print(tup[:])
print(tup[0:8:2])
