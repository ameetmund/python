# Branching and conditions

#
input1 = int(input("Enter the first number\t:"))
input2 = int(input("Enter the second number\t:"))

operation = int(input("Enter 1 - > Addition\n" 
                      "Enter 2 - > Subtraction\n" 
                      "Enter 3 - > Multiplication\n"
                      "Enter 4 - > Division\t:"))

if operation == 1:
    result = input1 + input2
    print(f"Addition of {input1} and {input2} is \t: {result}")
elif operation == 2:
    result = input1 - input2
    print(f"Subtraction of {input1} and {input2} is \t: {result}")
elif operation == 3:
    result = input1 * input2
    print(f"Multiplication of {input1} and {input2} is \t: {result}")
elif operation == 4:
    result = input1 / input2
    print(f"Division of {input1} and {input2} is \t: {result}")
else:
    print("Resulted in wrong operation")

# Using Boolean operations
# You will notice that the conditional operators are used in different way.
made_payment = True
paid = "Yes you have made the payment. No worries"
not_paid = "You have not paid the bill. Please pay soon"

print(paid) if made_payment else print(not_paid)


