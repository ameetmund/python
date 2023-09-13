def main():
    my_list = []
    list_length = int(input("Enter the length of the list: "))
    for i in range(list_length):
        num = input(f"Enter the {i} element: ")
        my_list.append(num)
    print(my_list)
    my_list.sort()
    print(my_list)
    print(my_list[1:0:-1])

if __name__ == '__main__':
    main()