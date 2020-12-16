# Dictionaries
# Simple dictionary and nested dictionary

my_dictionary = {'country':'India',
                 'state':'Karnataka',
                 'city':'Bangalore'}

print(my_dictionary)
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.get('state'))
my_dictionary['region'] = 'South'
print(my_dictionary)

# Getting each item in the dictionary and print them
# Remember to use .items() with the dictionary. Otherwise it will only
# result in key value
for key, value in my_dictionary.items():
    print(key, value)

# The following for loop will result in error
#for key, value in my_dictionary:
#    print("Printing without items", key, value)


countries = {'country':
                 {
                    'India':
                        {
                            'State':
                                {
                                    'Karnataka',
                                    'Punjab',
                                    'Maharastra',
                                    'Odisha',
                                    'TamilNadu'
                                }
                        },
                    'USA':
                        {
                            'State':
                                {
                                    'New York',
                                    'Missouri',
                                    'California',
                                    'Texas',
                                    'Florida'
                                }
                        },
                    'Australia':
                        {
                            'State':
                                {
                                    'NSW',
                                    'Tasmania',
                                    'Queensland',
                                    'Western Australia',
                                    'Victoria'
                                }
                        }
                 }
}

print(countries.keys())
print(countries.values())
print(countries['country']['India'])
print(countries['country']['India']['State'])
print(countries['country']['USA']['State'])
print(countries['country']['Australia']['State'])
print(countries.get('country'))