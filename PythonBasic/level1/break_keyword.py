newList = [10, 5, 48, 75, 92, 17]

newNum = int(input("Enter a number: "))

for i in newList:
    if i == newNum:
        print("Number is found")
        break
else:
    print("Number is not found")
