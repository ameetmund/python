# TODO: Lists are mutable set of values. 
# They can be changed, extended

myListOne = [5, 1.5, "Ameet"]
myListTwo = [10, 7.5, "Mund"]

# print(myListOne, myListTwo)
# print(myListOne[0])
# print(myListTwo[1:])
# print(myListOne*2)
# print(myListOne+myListTwo)

myListOne[1] = "2.5"
# print(myListOne)

# TODO: Tuples are non mutable. The values that are assigned 
# once can't be changed, but can be extended

myTupleOne = (5, 1.5, "Ameet")
myTupleTwo = (10, 7.5, "Mund") 

print(myTupleOne, myTupleTwo)
print(myTupleOne[0])
print(myTupleTwo[1:])
print(myTupleOne*2)
print(myTupleOne+myTupleTwo)

myTupleOne[1] = "2.5"
print(myListOne)