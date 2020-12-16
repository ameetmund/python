# List
# Functions and methods usage
# Adding methods - append, insert, extend
# Removing methods - remove, pop
# Reverse method
# Looping the list

# Following lists are containing numeric and string values
my_list = [903, 373, 223, 4031, 2033, 535, 677, 601, 161]
my_words_list = ['extreme', 'arrow', 'urgently', 'important', 'Urgent', 'imperative']

# Print the minimum and maximum value of list
print(min(my_list))
print(max(my_list))

# Print based on condition. Following are the two ways shown
print(True) if 'Urgent' in my_words_list else print(False)

if 'Urgent' in my_words_list:
    print(True)
else:
    print(False)

# Usage of a function 'sorted' to sor the list values and print it.
my_sorted_list = sorted(my_list)
print(my_sorted_list)

# Usage of a method 'sort()' to sort the value and print.
# You can observer that the method sort() doesn't return anything.
# So that means that the operations worked but it returned nothing.
# In this case the values are sorted. That can be seen when the list is printed
# But the assignment to new variable doesn't work as the return value is none
# This is because of some architectural rules that python addresses.
# So it's advised to use 'sorted' function instead of sort() method for assignment.
my_new_sort_list = my_list.sort()
print(my_new_sort_list)
print(my_list)

print(my_new_sort_list == my_sorted_list)

# Compares and prints the values of list
print(my_sorted_list == my_list)

########################################################################

# Append to a list
# We can see that the new value is appended into the list through append method
# But it it results nothing when it's assigned to a new list variable
# But the printed value of original lists shows that the value is appended
list_2 = [556, 21, 1007, 205, 176, 478]
append_list = list_2.append(757)
print(append_list)
print(list_2)

# Insert to a list
# We can see that the new value is inserted into the list through insert method
# New values is inserted into 2nd element in the list
# But it it results nothing when it's assigned to a new list variable
# But the printed value of original lists shows that the value is inserted
insert_list = list_2.insert(2, 2745)
print(insert_list)
print(list_2)

# Extend list
# New list values are appended into an existing list
# This can be done in two ways append and extend. The problem with append is
# that it will add the values as list into the existing list. But 'extend' adds
# it as a new value into the list
list_3 = [47, 589]
extend_list = list_2.extend(list_3)
print(extend_list)
print(list_2)

###########################################################################

# Remove list
# Specify the value that you would list to remove from the list and it will do.
remove_list = my_words_list.remove("Urgent")
print(remove_list)
print(my_words_list)

# Pop list
# It's similar to remove method, but it can't be used remove a specific value
# It can only be used to remove the last value in the list.
# But the value can be assigned to a variable and can be printed unlike 'remove'
pop_list = my_words_list.pop()
print(pop_list)
print(my_words_list)

# Reverse list
# This also results none, but it helps to reverse the list.
rev_list = my_words_list.reverse()
print(rev_list)
print(my_words_list)

#########################################################################
# Looping the list
for words in my_words_list:
    print(words)


