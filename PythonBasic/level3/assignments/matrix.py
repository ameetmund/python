# TODO 
# Assignment for 2*2 or 3*3 matrix
def main():
    num_rows = int(input("Enter number of rows you want: "))
    num_cols = int(input("Enter number of columns you want: "))
    matrix = []

    for rows in range(num_rows):
        inner_list = []
        for cols in range(num_cols):
            val = int(input(f"Enter the number of your choice for row {rows} & col {cols}: "))
            inner_list.append(val) 
        matrix.append(inner_list)
    print(matrix)

if __name__ == '__main__':
    main()