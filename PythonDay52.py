# def double(x):
#     return x * 2

# def apply(fx, value):
#     return 6 + fx(value)

apply = lambda fx, value: 6 + cube(value)

double = lambda x: x * 2 
cube = lambda x: x**3
avg = lambda x, y: (x + y) / 2

print(double(5))
print(cube(5))
print(avg(5, 10))
print(apply(cube, 2))