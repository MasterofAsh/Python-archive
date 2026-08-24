class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Sound made by the animal")

    def eat_food(self):
        print("Food eaten by the animal")

    def showDetails(self):
        print(f"Name: {self.name} \nSpecies: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")

    def eat_food(self):
        print("Meat, bones, chicken, dog food")

    def showDetails(self):
        Animal.showDetails(self)
        print(f"Breed: {self.breed}")

class Shiba_Inu(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed = "Japanese")
        self.color = color

    def make_sound(self):
        print("Bark Bork.... click click click BORK!")

    def eat_food(self):
        print("Meat, bones, chicken, dog food")

    def showDetails(self):
        Dog.showDetails(self)
        print(f"Color: {self.color}")

c = Shiba_Inu("Doge", "Light Brown")
c.showDetails()