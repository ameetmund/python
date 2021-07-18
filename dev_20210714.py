# # Check driver age and print required messages
# def checkDriverAge(age=0):
#     '''
#     Checks drivers age for safety purpose
#     '''
#
#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!");
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")
#
# checkDriverAge()
#
# # *args and **kwargs
# # Rule: always use the order when using *args and **kwargs.
# # Order to follow is - positional parameters, *args, keyword parameters, **kwargs
# # Practically all the parameters are usually not given at once. Mostly it's two of them.
#
# def get_sum(*args, **kwargs):
#     total = 0
#     for item in kwargs.values():
#         total += item
#     return print(sum(args) + total)
#
# get_sum(1,2,3, num1=5, num2=10)


def highest_even(my_list):
    '''
    print the highest even number in the list
    '''
    my_list.sort(reverse=1)
    for item in my_list:
        if item % 2 == 0:
            return print(f'Highest even number found is {item}')
    return print('No even number was found')

highest_even([105, 1, 1, 42, 3, 16, 65, 71])

my_list = [1, 1, 2]
print(set(my_list))