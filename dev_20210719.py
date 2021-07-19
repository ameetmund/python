# Functional programming
# Lambda functions or expressions.
# Lambda's are mainly used when we have to meet one time need. It's equivalent
# to a function, but then we don't have to create a new function for that.

from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

print(list(map(lambda item: item.upper(), my_pets)))

#2 Filter the scores that pass over 50% using lambda
scores = [73, 20, 65, 19, 76, 100, 88]

print(list(filter(lambda item: item > 50, scores)))

#3 Reduce using lambda
my_numbers = [5,4,3,2,1]
scores = [73, 20, 65, 19, 76, 100, 88]

print(reduce(lambda acc, item: acc+item, (my_numbers+scores)))

#4 Square of list items using lambda
my_list = [5, 4, 3, 3]
print(list(map(lambda item: item**2, my_list)))

#5 List sorting using lambda
my_new_list = [(0, 2), (4, 3), (9, 9), (10, -1)]
my_new_list.sort(key=lambda item: item[1])
print(my_new_list)

#6 List, Set & Dictionary comprehensions
# Comprehensions are only useful when it's not overly done or complicated
# Never try to complicate the comprehension, instead write the code
# in a separate function. Following are some of the simple list comprehensions
# example.
list_comp = [item*2 for item in my_list]
print(list_comp)

set_comp = {item*2 for item in my_list}
print(set_comp)

my_dict = {
    'a': 1,
    'b': 2
}
dict_comp = {k:v**2 for k,v in my_dict.items()}
print(dict_comp)

dict_comp_new = {v:v**2 for k,v in my_dict.items()}
print(dict_comp_new)



