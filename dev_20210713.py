my_list = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

print(my_list)

# Iterate over my_list
#   If the value is 0 then replace with spaces
#   If the value is 1 then replace with *

for key1, value1 in enumerate(my_list):
    for key2, value2 in enumerate(value1):
        if value2 == 0:
            my_list[key1][key2] = ' '
            print(' ', end='')
        elif value2 == 1:
            my_list[key1][key2] = '*'
            print('*', end='')
        else:
            print("Wrong input value")
        # print(value2)
        # print(my_list[key1][key2])
    print(' ')

print(my_list)

# Find the duplicates in the list
    # Method 1 - Not very efficient
new_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

new_list.sort()
for key, value in enumerate(new_list):
    if new_list[key] == new_list[key-1]:
        print(f'{value} is repeated')


# Find the duplicates in the list
    # Method 2 - Better than previous
duplicates = []
for value in new_list:
    if new_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)


'''
Let's begin Function.
Functions are the best way to keep the repeatitive codes in one
place and use them again and again.
'''

def duplicate():
    # Iterate over my_list
    #   If the value is 0 then replace with spaces
    #   If the value is 1 then replace with *
    my_list = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ]

    for key1, value1 in enumerate(my_list):
        for key2, value2 in enumerate(value1):
            if value2 == 0:
                my_list[key1][key2] = ' '
                print(' ', end='')
            elif value2 == 1:
                my_list[key1][key2] = '*'
                print('*', end='')
            else:
                print("Wrong input value")
            # print(value2)
            # print(my_list[key1][key2])
        print(' ')

    print(my_list)

# Make a call to the duplicate function
duplicate()

# Parameters and arguments -
    # Parameters are part of functions
    # Arguments are values that are passed to functions
# Function parameters
    # Positional parameter - It follows the order as defined
    # Keyword parameter - Pass the arguments using keywords
    # Default parameter - Defines default values

# Example of function using positional parameter
def say_hello(name):
    print(f'Hello {name}')

say_hello("John")

# Example of function using keyword parameter
def say_hi(name, emoji):
    print(f'Hello {name} {emoji}')

say_hi(emoji=':-)', name='Jack')

# Example of function using default parameter
def say_hi(name='World', emoji=':-)'):
    print(f'Hello {name} {emoji}')

say_hi()