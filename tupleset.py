# Tuple & Set

my_tuple = ('1', 'John', 'USA')
print(type(my_tuple))
print(my_tuple[2])
print(my_tuple.count(2))
#my_tuple[2] = 'India'       # Tuple is immutable. So we can't change an item
my_tuple = ('2', 'Jack', 'Australia')   # But the entire tuple can be replaced
print(my_tuple)


my_set1 = {1,2,3,4,5, 'John', 'Snow'}
my_set2 = {5,3,2,1,6, 'Snow'}
print(my_set1)
print(my_set2)
print(my_set1.difference(my_set2))
print(my_set1.union(my_set2))
