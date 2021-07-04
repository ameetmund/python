# 2D list

list_num = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in list_num:
    print(row)

for row in list_num:
    for col in row:
        print(col)


# Try Except

try:
    number = 10/1
    print(int(input("Enter a number: ")))
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input")

# File read
window_file = open("F:\Python\PythonProject\Github\python\data\windowdata.csv", "r")
for rec in window_file.readlines()[1:3]:
    print(rec)
window_file.close()


# Import
import datetime

now_time = datetime.datetime.now()
later_time =  datetime.datetime.utcnow()
diff = later_time - now_time
print(diff)
