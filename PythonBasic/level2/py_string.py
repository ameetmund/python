# name = "Ameet"
# score = 95

# print("The score of " + name + " is: ", score)
# print(f"The score of {name} is {score}")

name = input("Please enter the name: ")
print(name.isnumeric())
if name.isnumeric():
    print("Please enter char values between A-Z")
else:
    name = name.strip()
    print(name)

