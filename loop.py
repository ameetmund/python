# For Loops
# Generators
# While loops


# Find the sum of list1
list1 = (1, 3, 6, 2, 8, 10, 7)
sum = 0

for num in list1:
    sum += num
print(f"The sum using list is {sum}")

# Use of range
# This will give a range of numbers between 0 and specified number
print(range(10))
print(list(range(10)))

sum = 0
for num in range(len(list1)):
    sum += list1[num]

print(f"The sum using range is {sum}")

# There is a way to start the first element of range from 1 instead of 0
# Step size can also be given to find alternate numbers

print(range(1, 11))
print(list(range(1, 11)))
print(list(range(1, 20, 2)))


# While loop
num1 = 0
while num1 < 10:
    num1 += 1
    print(num1)




