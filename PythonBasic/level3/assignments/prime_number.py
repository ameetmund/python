# Prime number is a number which can be divided by itself only
def main():
    num = int(input("Enter a number of your choice: "))
    for i in range(2, num):
        rem = num % i
        # print(num, i, rem)
        if rem == 0:
            break
    if rem == 0:
        print("Not a prime number")
    else:
        print("Congratulation - It's a prime number")

if __name__ == '__main__':
    main()