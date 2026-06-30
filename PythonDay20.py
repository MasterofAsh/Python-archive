a = int(input("Enter your number: "))
b = int(input("Enter your second number: "))

def squareCalculator():
    formula1 = (a*a) + (b*b) + (2 * (a*b))
    print(formula1)

    formula2 = (a*a) + (b*b) - (2 * (a*b))
    print(formula2)

squareCalculator()


def isGreater():
    if (a > b):
        print("a is greater than b")
    else:
        print("b is greater than a")
isGreater()