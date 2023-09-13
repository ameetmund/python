def main():
    num_list = []
    no_of_elements = int(input("Please enter number of elements for which you need average: "))
    for i in range(no_of_elements):
        num = int(input(f"Please enter number {i+1}: "))
        num_list.append(num)
    print(num_list)
    sum = 0
    for j in range(len(num_list)):
        sum = sum + num_list[j]
    print(sum)
    avg_of_list = round((sum/len(num_list)), 2)
    print(avg_of_list)

if __name__ == '__main__':
    main()