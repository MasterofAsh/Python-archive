x = 4
print(f"The global x is: {x}")

def hello():
    x = 6
    y = 64
    print(f"The local x is: {x}")

hello()

print(x)

# print(y) # variables created in a function can only be called in the respective function

# 2 variables, global and local can be of the same name.
# A global variable can be used inside functions, whereas a local cannot be used globally or inside other functions
# Same name global and local variables can be created to have different or same values

# Local variables (variables in a function) are deleted after the execution of a function and its completion

