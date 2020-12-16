# List comprehension
# While loop with break
# Enumerate

# Generate 20 random numbers between 1 to 100
# Please note that these random number will not be in an order
# For this we need to import few libraries
import random
import string

list1 = []

for num in range(20):
    list1.append(random.randint(1, 100))
print(list1)


# Above For loop can be fit into the list as well which is as below
list2 = [random.randint(1, 100) for num in range(20)]
print(list2)

# The items can be ordered as well
list3 = [num for num in range(20)]
print(list3)

# Get random characters as well by using CHOICE
list4 = [random.choice(string.ascii_uppercase) for num in range(10)]
print(list4)

# While loop with break
# It comes out of the loop the moment condition is met
list5 = [random.randint(1, 30) for num in range(20)]
print(list5)
num1 = 0
while num1 < len(list5):
    if list5[num1] == 30:
        print(f"The index found for first occurance of 30 is {num1}")
        break
    num1 += 1


# Use of enumerate
list6 = [random.randint(1, 15) for num in range(20)]
print(list6)
for index, num in enumerate(list6):
    if num == 10:
        print(f"The first index for 10 is {index}")
        break

# Use of zip
# This will concatenate two lists and result will be a list of tuples
list7 = ('python', 'javascript')
list8 = ('.py', '.js')

zipped_list = list(zip(list7, list8))
print(zipped_list)

