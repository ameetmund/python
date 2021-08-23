import random

def rand():
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input("Please enter a Number: "))
            if 0 < guess < 11:
                if guess == answer:
                    print("You are genius")
                    break
            else:
                print("It only expects 1~10")
        except ValueError:
            print("Please enter a numerical value")
            continue

if __name__ == '__main__':
    rand()


