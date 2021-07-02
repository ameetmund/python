# Guessing game
secret_code = "python"
guess = ""
max_guess = 3
out_of_guess = False
guess_count = 0

while guess != secret_code and not(out_of_guess):
    if guess_count < max_guess:
        guess = input("Enter Your Secret Code: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("You Are Out Of Luck")
else:
    print("Wooohooo You Win A Jackpot")


# For loop

for char in "python":
    print(char)

list1 = ["John", "Jack", "Jill", "Jim"]
for item in range(len(list1)):
    print(list1[item])

# Exponent function
def exp_func(base_num, power_num):
    result = 1
    for pow in range(power_num):
        result = result * base_num

    return result

print(exp_func(3, 2))




