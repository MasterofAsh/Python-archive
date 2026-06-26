x = int(input("Enter a numeric value for x: "))
match x:
    case 0:
        print("x is 0")
    case 5:
        print("x is 5") 
    case _ if x > 90:
        print("x is greater than 90")
    case _ if x == 90:
        print("x is 90")