class Animal:
    def __init__(self, name, species):
        self.species = species
        self.name = name
    
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")

d = Dog("Suraiya", "Huskie")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

# Quiz: Implement a Cat Class from Animal class with its unique methods

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Cat")
        self.breed = breed

    def make_sound(self):
        print("Meow!")

    def catPurr(self):
        print("Purrr!! Purrr!!!")

c = Cat("Mano", "Persian")
c.make_sound(), c.catPurr()