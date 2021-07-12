'''
Difference between sort() method and sorted() function
sorted() function doesn't change the original value of the list. In fact it just
creates a new object. sort() method changes the original list though. Please note
that it returns None. So you can't use sort() method in print.
'''
char_list = ['a', 'f', 'z', 'h', 'd', 'b', 'c', 'y']

print(sorted(char_list))
print(char_list)

char_list_2 = char_list.copy()
char_list_2.remove('y')
print(char_list)
print(char_list_2)

char_list.sort()
print(char_list)

# join also helps in adding a specific object to each indices of the list
greet_list = " ".join(['hello', 'my', 'name', 'is', 'Mark'])
print(greet_list)


# range is used widely with list
print(list(range(5, 15)))
print(len(list(range(5,15))))

# list unpacking helps to get the values to respective variables
a, b, c = [1,2,3]
print(a, b, c)

a, b, c, *others = [1, 2, 3, 4, 5, 6, 7]
print(a, b, c, others)


'''
Dictionaries are another type of data structures in python. They are similar to hash 
tables is some of the other languages. Dictionaries are un-ordered. So it provides
an efficient way of handling with data
'''
my_dictionary = {
    'first_name': "John",
    'last_name': "Andrew",
    'country': "USA"
}

print(my_dictionary['first_name'], my_dictionary['last_name'], my_dictionary['country'])

print(my_dictionary.get("country"))
print(my_dictionary.get("city"))    # It will provide None as nothing is present as
                                    # a "city" key.

my_dictionary.pop('country')        # It will remove country from the dictionary
print(my_dictionary)

print(my_dictionary.keys())
print(my_dictionary.values())

print(my_dictionary.update({"city":"New York"}))
print(my_dictionary)

new_game = {
    'age': 21,
    'username': 'jack_matt',
    'weapons': ['bullets', 'guns', 'rifles'],
    'is_active': True,
    'clan': False
}

print(new_game.keys())
new_game['weapons'].append('shield')
print(new_game)

new_game.update({'is_banned':False})
print(new_game)

new_game.update({'is_banned':True})
print(new_game)

# It is important to note that.copy method ensures that the new object is just a
# copy of the original one and the original doesn't get the changed value from the
# copied dictionary. This rule is applicable for list as well.

new_game_2 = new_game.copy()
new_game_2.update({'age':25, 'username':'johny_john'})
print(new_game)
print(new_game_2)


