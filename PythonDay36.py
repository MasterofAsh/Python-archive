a = input("Enter your number: ")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} is: ", (int(a) * i))
except:
    print("Invalid Input")

print("End of program")
print("Finishing program")

try:
    num = int(input("Enter your number"))
    a = [5, 6]
    print(a[num])
except ValueError:
    print("Value is not an integer")
except IndexError:
    print("Value of out index range.")