india_cities = ["Delhi", "Mumbai", "Bangalore"]

usa_cities = ["WashingtonDC", "NewYork", "Chicago"]

# print list
print(india_cities, usa_cities)
print(india_cities[2])

# delete list
del india_cities[1]
print(india_cities)

# other list operations
india_cities.insert(1, "Mumbai")
print(india_cities)

usa_cities.pop()
print(usa_cities)

usa_cities.append("St.Louis")
print(usa_cities)
