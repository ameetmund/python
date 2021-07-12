is_magician = True
is_expert = False

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not(is_expert):
    print('Atleast you\'re getting there')
else:
    print("You need magic powers")


# Difference between is and ==
# == compares only the values
# is compares the memory locations where it's present

print(1 == 1)
print(True is 1)
print(1 is 1)

print('1' == '1')
print('1' is '1')

print([1, 2] is [1, 2])

is_student = True
is_boy = True

print(is_boy is is_student)


'''
For loops using dictionaries and list
'''
my_dict = {
    'name': 'John',
    'age': 50,
    'city': 'New York'
}
for item in my_dict:
    print(item)

for item in my_dict.items():
    print(type(item))
    print(item)

for key, value in my_dict.items():
    print(f'{key} is {value}')

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_num = 0
for num in my_list:
    sum_num += num
print(f'Sum of all the numbers is: {sum_num}')

# enumerate - This is useful when we need the index along with the value in a loop
for i, num in enumerate(list(range(100))):
    if num == 50:
        print(f'The index is {i}')

# break, continue, pass
# We will notice that continue and pass does nothing. Continue just passes the control
# to the start of the loop and pass just does nothing. It's useful only when we are
# not sure what to do.
for i, num in enumerate(list(range(100))):
    if num == 50:
        print(f'Using break statement - The index is {i}')
        break

for i, num in enumerate(list(range(100))):
    continue
    if num == 50:
        print(f'The index is {i}')

for i, num in enumerate(list(range(100))):
    # if num == 50:
    #     print(f'The index is {i}')
    pass