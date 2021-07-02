import bisect
from bisect import bisect_left

list1 = [10, 12, 30, 45, 20]
index = 0

list1.sort()
print(list1)

if(bisect.bisect_left(list1, 15)):
    print("number exists")
else:
    print("doesn't exist")




