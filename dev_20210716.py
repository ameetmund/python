# OOP concepts
class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Meaow(Cat):
    def sing(self, sounds):
        return f'{sounds}'

cat1 = Simon('Mee', 1)
cat2 = Sally('Mee Mee', 2)
cat3 = Meaow('Meaow', 3)
my_cat = [cat1, cat2, cat3]


my_pet = Pets(my_cat)
my_pet.walk()