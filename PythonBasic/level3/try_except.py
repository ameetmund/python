# TODO operation without error
# def main():
#     try:
#         myFile = open("myFile.txt", "r")
#         print("Successfully opened the file")
#     except IOError:
#         print("File was not found")
    
#     print("Program execution is completed")

# TODO operation with error
def main():
    try:
        myFile = open("myFil.txt", "r")
        print("Successfully opened the file")
    except IOError:
        print("File was not found")
    
    print("Program execution is completed")


if __name__ == '__main__':
    main()