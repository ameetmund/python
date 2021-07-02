def find_max(num1, num2, num3):
    num4 = max(num1, num2, num3)
    return num4

max_num = find_max(1, 2, 5)
print(max_num)

month_conversion = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"

}

print(month_conversion.get(15, "Not a valid key"))

is_true = True
find_num = 0
add_num = 0
while(is_true and find_num <= 10):
    add_num = add_num + 1
    find_num = find_num + 3
    if find_num > 10:
        is_true = False
print(add_num, find_num)