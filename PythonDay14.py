# a = int(input("Enter your age: "))
# print("Your age is: ", a)

# if(a > 18):
#     print("You can drive any vehicle.")
# else:
#     print("Come back when you are older.")

# num = int(input("Enter your number: "))
# if (num < 0):
#     print("The number is negative")
# elif (num == 0):
#     print("The number is zero")
# elif (num > 0):
#     print("The number is positive")
# else:
#     print("Please enter a valid number")

grade = "null"
marks = int(input("Please enter your SSC marks: "))
if (marks == 990):
    print("You have a 90%")
    grade = "A"
    print(grade)
    if (grade == "A"):
        print("You are among the top 27 students in the school")
elif (marks > 880):
    print("You have a percentage of 80%")
    grade = "B+"
    print(grade)
    if (grade == "B+"):
        print("You are among the top 50 students in the school")
else:
    print("Sorry, this result only includes students who scored more than 80 percent of marks.")