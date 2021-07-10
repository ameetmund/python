# Lists

amazon_shopping = ["pens", "t-shirt", "coffee mug", "water bottle"]

print(amazon_shopping)
print(amazon_shopping[0:3])

new_cart = amazon_shopping
print(new_cart)
print(amazon_shopping)

new_cart[0] = "pencils"
print(new_cart)
print(amazon_shopping)

amazon_shopping[1] = "pant"
new_cart = amazon_shopping[:]   # IMPORTANT concept when we assign list.
                                # DO NOT simply assign without [:], else new list will
                                # also point to the same memory location.
                                # Any change in new list will reflect in the old one as well.


new_cart[1] = "cap"
print(new_cart)
print(amazon_shopping)

'''
Matrix - Multi dimensional list.
It's mainly used in AI and ML
'''

matrix = [
    [1, 6, 8],
    [3, 5, 7]
]

print(matrix[1][2])


'''
List methods - Very useful way of dealing with list especially when adding or removing items
'''

amazon_shopping.append("phone")
print(amazon_shopping)

amazon_shopping.insert(0, "Drawing board")
print(amazon_shopping)

amazon_shopping.extend(["laptop", "TV", "Refrigerator"])
print(amazon_shopping)

print(amazon_shopping.append("sunglass"))   # This will print None as the list method doesn't
                                            # produce any result

print(amazon_shopping)

amazon_shopping.pop()
print(amazon_shopping)

amazon_shopping.remove("phone")
print(amazon_shopping)

amazon_shopping.clear()
print(amazon_shopping)