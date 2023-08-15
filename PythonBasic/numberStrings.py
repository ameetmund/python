# ****** Integers *********
# In python real numbers and floats are defined in different 
# ways. 

# realNumber = 10
# floatNumber = 10.0

# print(type(realNumber))
# print(type(floatNumber))

# Also special care is required while taking input of numbers
# and do some operation using it. Because the sum may not result
# in numbers. 
# numberOne = input("First number: ")
# numberTwo = input("Second number: ")

# print(numberOne + numberTwo)

# The above one will result in strings. So in order to avoid it
# it must be explicitly defined as integer

# numberOne = int(input("First number: "))
# numberTwo = int(input("Second number: "))

# print(numberOne + numberTwo)

# ********** Integer - End *********

# ********** String - Start ********
# Strings always start from position 0 instead of 1
firstName = "Ameet"
lastName = "Mund"

fullName = firstName + lastName
print(fullName)
print(fullName[0])
print(fullName[3])
print(fullName[2:])
print(fullName[0:3])
print(fullName[-1])
print(fullName[:5:-1])