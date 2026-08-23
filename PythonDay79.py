class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is: {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is: {self.dance}")

class DancerEmployee(Dancer, Employee):
    def __init__(self, name, dance):
        self.dance = dance
        self.name = name

    def __str__(self):
        return f"{self.name} and {self.dance}"

o = DancerEmployee("Umar", "Nachaiya")
o.show() # The class which is mentioned first as a parameter in the child class will be printed, in this case, the Dancer class
print(DancerEmployee.mro()) # Allows us to see the order in which the methods are applied
# Dancer Employee (Class) -> Dancer (Class) -> Employee (Class)