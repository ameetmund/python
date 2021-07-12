# Tuple and Set

my_tuple = ('a', 'b', 'c', 'd', 'd')
print(my_tuple)
print(my_tuple.count('d'))
print(my_tuple.index('d'))

#Tuples are immutable and the values can't be changed once assigned
# my_tuple[4] = 'e'
#
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)
my_list = list(my_tuple)
my_list = [1, 2, 3, 4, 5]
print(my_list)

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 9}
print(my_set)
print(list(my_set))


