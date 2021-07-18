# Functional programming
# Important thing to understand in functional programming is to keep
# the data and function separately. A function must always return only
# one value, no matter how many times the same data is given. It
# should never change it's value
# map, filter, zip, reduce are some of the functions that are used in
# functional programming.

from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(pets):
    return pets.upper()

print(list(map(capitalize, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def student(score):
    return score > 50


print(list(filter(student, scores)))

def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers+scores), 0))