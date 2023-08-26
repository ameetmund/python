def main():
    # my_file = open("myFile.txt", "w")
    # for i in range(10):
    #     my_file.write(f"This is number {i} \n")
    # my_file.close()

    my_file = open("myFile.txt", "r")
    print(my_file.read())
    my_file.close()
    
if __name__ == '__main__':
    main()
