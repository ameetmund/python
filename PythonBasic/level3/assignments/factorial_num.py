# TODO
# Factorial numbers are the multiplied values of all the numbers
# between that number all the way upto 1

def main():
    num = int(input("Please enter a number of your choice: "))
    if num <= 0:
        print("Please enter a positive value greater than 0")
    else:
        fact_num = 1
        for i in range(1, num + 1):
            fact_num = fact_num * i
        print(f"Facotial of {num} is {fact_num}")

if __name__ == '__main__':
    main()