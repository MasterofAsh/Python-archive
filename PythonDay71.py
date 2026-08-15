# x = [1, 2, 3]
# print(dir(x))
# print(x.__add__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p = Person("Ahmed", 35)
print(p.__dict__)

print(help(Person))