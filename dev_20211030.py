#Merge sorted list

def merge_sorted(list1, list2):
    # for i in list2:
    #     list1.append(i)
    #
    # print(list1)

    # prev_item = 0
    # for i, j in enumerate(list1):
    #     if i <= len(list1):
    #         if j > prev_item:
    #             prev_item = j
    #         elif j == prev_item:
    #             prev_item = j
    #         else:
    #             list1[i-1], list1[i] = list1[i], list1[i-1]
    #
    # print(list1)
    print(len(list1), len(list2))
    sorted_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i += 1
        elif list1[i] == list2[j]:
            sorted_list.append(list1[i])
            sorted_list.append(list2[j])
            i += 1
            j += 1
        else:
            sorted_list.append(list2[j])
            j += 1
    print(i, j)
    if i < j:
        sorted_list = sorted_list + list1[i:]
    else:
        sorted_list = sorted_list + list2[j:]

    print(sorted_list)


merge_sorted([0, 3, 4, 31], [])


list1 = [0, 3, 4, 31]
list2 = [4, 6, 30]

print(sorted(list1 + list2))