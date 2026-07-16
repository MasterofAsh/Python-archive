# for i in range(5):
#     print(i)
# else:
#     print("Sorry, no \'i\' was found")

for i in []:
    print(i)
else:
    print("Sorry, no \'i\' was found")

students = 1
x = 0
while x < 10:
    print(f"This is Student: {students}")
    students = students + 1
    x = x + 1
    # if (students == 7):
    #     print("This is a special student, breaking loop.")
    #     break
else:
    print("No more students left.")

# The else after loops only initiates if the loop finishes entirely. If the loop breaks, the else doesnt count.