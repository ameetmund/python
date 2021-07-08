weather = 'It\'s "sunny\t-Great!\n"I want to go out"'
print(weather)

name = 'Johny'
age = 55

print("Hey " + name + ". You are " + str(age) + " years old")

# Same content by using formatted string operator. It makes it clean
print(f'Hey {name} You are {age} years old')

# Indexes
# [start:stop:step over]
num = '0123456789'
print(num[0:10:1])
print(num[0:])
print(num[0:3])
print(num[0:10:2])
print(num[0::2])
print(num[::2])
print(num[::-1])

print(num.replace('9', '2'))