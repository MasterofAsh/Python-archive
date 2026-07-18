def indexErrorFunc():
    try:
        a = [1, 2, 3, 4, 5]
        print(a)
        i = int(input("Enter the index you want: "))
        print(a[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I am always executed.")

x = indexErrorFunc()
print(x)