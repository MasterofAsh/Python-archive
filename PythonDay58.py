class Person:
    def __init__(self, name, occ):
        print("This is being called")
        self.Name = name
        self.Occ = occ
    def info(self):
        print(f"{self.Name} is a {self.Occ}")

a = Person("Abdullah", "Worker")
b = Person("Kumulala", "CEO")
a.info()
b.info()