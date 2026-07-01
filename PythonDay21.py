# Function Arguements
# Four Types of Arguements:
"""
Default Arguements
Keyword Arguements
Variable Arguements
Required Arguemnets
"""

# def averageCalc(a = 3, b = 5):
#     print("The average1 is: ", (a+b)/2)
# averageCalc(5, 5)   # Arguement provided later on
# averageCalc()       # No arguement provided
# # Default arguements: Values for parameters provided in the creation of a function will be 
# # used if no other arguements are provided later on. If an arguement is provided later on
# # then the default arguement will be ingored

# # Keyword arguements allow for the ordering of arguements by the choice of the user
# averageCalc(b = 21, a = 9)

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        return sum / len(numbers)

c = average(5, 6, 7, 1)
print(c)