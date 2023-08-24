# def calculateSum(inputs):
#     i = 1
#     total = 0
#     while(i <= inputs):
#         num = int(input("Enter the next number: "))
#         total = total + num
#         i = i + 1
#     print(total)

def productPrice(*inputs):
    difference = 0
    if len(inputs) == 2:
        difference = abs(inputs[0] - inputs[1])
    else:
        print("Numbers must be limited to 2 only")
    print(difference)

productPrice(500, 300, 100)