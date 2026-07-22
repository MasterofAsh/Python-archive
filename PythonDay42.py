# Enumerate function
marks = [12, 54, 97, 24, 34, 22, 50]

# index = 0
# for mark in marks:
#     print(mark)
#     if (index == 2):
#         print("deez nuts")
#     index += 1

for index, mark in enumerate(marks):
    print(mark)
    if (index == 2):
        print("deez nuts")

fruits = ["apple", "banana", "mango", "dragon fruit", "grapes"]
for index, fruit in enumerate(fruits):
    print(index + 1, ": ", fruit)