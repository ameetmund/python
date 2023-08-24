import sub_module

user_input = int(input("Enter your choice 1. Add, 2. Subtract, 3. Multiply, 4.Division: "))

if user_input == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(sub_module.addNum(num1, num2))
elif user_input == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(sub_module.subNum(num1, num2))
elif user_input == 3:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(sub_module.mulNum(num1, num2))
elif user_input == 4:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(sub_module.divNum(num1, num2))
else:
    print("Enter any number between 1 to 4")