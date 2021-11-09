#First recurring character

my_list1 = [2, 5, 1, 2, 3, 5, 1, 2, 4]
my_list2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
my_list3 = [2, 3, 4, 5]

def recur(my_list):
    i = 0
    j = i+1
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            if my_list[i] == my_list[j]:
                return my_list[j]

print(recur(my_list1))

def hash(my_list):
    my_dict = {}
    for i in range(len(my_list)):
        if my_list[i] == my_dict.values():
            return my_list[i]
        else:
            my_dict[i] = my_list[i]
    print(my_dict)
print(hash(my_list1))


recur(my_list1)