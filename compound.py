# Compound data types
# List, Dictionaries, Sets & Tuples

# List
list = [1,2,True,"John",None,5.0]
print(list)
print(list[2])
print(list[5])
list[3] = "Jack"
print(list[3])
print(list)

# Dictionaries
# These are combination of key and value pair
dict = {'name': 'Harry', 'age': '50'}
print(dict)
print(dict['name'])
print(dict['age'])
dict['name'] = 'Glen'
print(dict)

# Sets
# Sets are similar to Lists. But there are no ordering in the output
# Also you can't print a particular indexed value as it doesn't support order
sets = {1,2,False,"John",None,5.0}
print(sets)
#print(sets[2])
#print(sets[5])
#sets[3] = "Jack"
#print(sets[3])
#print(sets)

# Tuples
# These are similar to lists, but they are immutable
tup = (1,2,False,"John",None,5.0)
print(tup)
print(tup[1])
print(tup.index('John'))
#tup[2] = True
#print(tup)
