# Numbers will remain as it is even if it's reveresed
def main():
    num = input("Enter a number: ")
    # print(num[0:])
    # print(num[::-1]) 
    if num[0:] == num[::-1]:
        print("It's a Palindrome")
    else:
        print("Try your luck with another number :-( ")
    

if __name__ == '__main__':
    main()