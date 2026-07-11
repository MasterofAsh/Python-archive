# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(3))

# Functioning Fibonacci Sequence
"""
f0 = 0
f1 = 1
f2 = f1 + f0

Fn = f(n-1) + f(n-2)
"""

def fibonacciSeq(n):
    if (n <= 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return (fibonacciSeq(n - 1) + (fibonacciSeq(n - 2)))

steps = 10
sequence = [fibonacciSeq(n) for n in range(steps)]
print(sequence)
