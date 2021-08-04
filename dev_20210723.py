# Error handling & Generators

from datetime import datetime

def check_age(age):
    try:
        if int(age) < 5:
            print("You are a Toddler")
        elif age >= 5 and age <= 10:
            print("You are a kid")
        elif age > 10 and age <= 18:
            print("You are growing fast")
        elif age > 18 and age <= 40:
            print("You are adult and still young :-) ")
        elif age > 40 and age <= 60:
            print("You are growing old")
        else:
            print("You are old")
    except ValueError and TypeError:
        print("Please enter a valid number")



print(check_age(input("Enter your age: ")))

# Fibonacci using generators
def fibonacci_gen(n):
    '''Build and return using a generator '''
    first_num = 0
    next_num = 1
    for item in range(n):
        yield first_num
        temp = first_num
        first_num = next_num
        next_num = temp + next_num

in_time = datetime.now()
for i in fibonacci_gen(10000):
    print(i)
out_time = datetime.now()
time_diff = out_time - in_time
print(f'Time to generate sum with generator is: {time_diff}')

# Fibonacci using a list
# def fibonacci_list(n):
#     first_num = 0
#     next_num = 1
#     result = []
#     for i in range(n):
#         result.append(first_num)
#         temp = first_num
#         first_num = next_num
#         next_num = temp + next_num
#     return result
#
# in_time = datetime.now()
# print(fibonacci_list(100000))
# out_time = datetime.now()
# time_diff = out_time - in_time
# print(f'Time to generate sum without generator is: {time_diff}')

