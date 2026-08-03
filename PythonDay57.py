class Person:
    name = "Harry"
    occupation = "Software Developer"
    netWorth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
# a.name = "Abdullah"
# a.occupation = "Accountant"
# print(a.name, a.occupation)
a.info()