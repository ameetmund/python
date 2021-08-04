import random
import sys

random_number = random.randint(1, 10)
input_number = 0
chance = 0
while random_number != input_number:
    chance += 1
    input_number = int(input("Guess the number: "))
    if random_number == input_number:
        print("Bang on target. You WIN")
        print(f'You attempted {chance} times')
    else:
        print("Try your luck next time")
