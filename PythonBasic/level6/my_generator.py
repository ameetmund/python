# Generator function provides series of values through yield
# statement. This is different than return as return only provides
# one single value.
import random

def main():
    print_rand()

def print_rand():
    generate_rand()
    for num in generate_rand():
        print(num)

def generate_rand():
    for i in range(1, 6):
        yield random.randint(1, 99)

if __name__ == '__main__':
    main()