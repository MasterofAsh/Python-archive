class Employee:
    def __init__(self, name):
        self.name = name

    name = "harry"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    
    def __str__(self):
        return (f"The name of the employee is {self.name} __str__")
    
    def __repr__(self):
        return (f"The employee is {self.name} __repr__")
    
    def __call__(self):
        print("Hey, it's me! Goku")