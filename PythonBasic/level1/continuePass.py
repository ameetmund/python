newList = [10, 5, 48, 75, 92, 17]

newNum = int(input("Enter a number: "))

# Continue is used to skip one particular value(s)
# for i in newList:
#     if i == newNum:
#         continue
#     print(i)
# else:
#     print("Number is not found")

# Pass is used to fill a dummy operation
for i in newList:
    if i == newNum:
        pass
    print(i)

