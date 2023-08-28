# Prime number is a number which can be divided by itself only
def main():
    lower_range = int(input("Enter a lower number of your choice: "))
    upper_range = int(input("Enter a upper number of your choice: "))
    for num in range(lower_range, upper_range):
        for i in range(2, num):
            rem = num % i
            # print(num, i, rem)
            if rem == 0:
                break
        if rem == 0:
            print(f"{num} is not a prime number")
        else:
            print(f"Congratulation - {num} is a prime number")

if __name__ == '__main__':
    main()