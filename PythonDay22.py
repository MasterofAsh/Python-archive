# Lists are ordered collection of different data types
# They are enclosed within [] brackets and separated by commas
# Content can be added in a list afterwards unlike a Tuple

marks = [3, 5, 6, "Kumosla", "AAAAAAAAAGH", 4, 69, 420]

print(marks)
print(type(marks))
print(marks[0])

if "umer" in marks:
    print("deez nuts")
else:
    print("nani")

if "kumo" in marks:
    print("Yes")
else:
    print("NO")

print(marks[0:7:2])