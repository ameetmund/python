# Function
# OOP Cat exercise
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiating new cat objects out of a Cat class
cat1 = Cat("Meow1", 1)
cat2 = Cat("Meow2", 3)
cat3 = Cat("Meow3", 2)

def cat_age(cat1, cat2, cat3):
    age_list = [cat1.age, cat2.age, cat3.age]
    age_list.sort(reverse=1)
    print(f'The oldest cat is {age_list[0]} years old')

check_cat_age = cat_age(cat1, cat2, cat3)



