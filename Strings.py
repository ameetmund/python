# Strings #

# Print using single quote #
print('This is the way we use single quotes in python :-)')

# Print using double quotes #
print("This is the way we use double quotes in python :-)")

# Print using triple quotes #
print("""
      This is 
      the way
      we use
      triple quotes
      in python
     """)

# Print single quote within double quote #
print("I'm using single quote within double quote")

# Print single quote using escape character #
print('I\'m using single quote with escape character')

# Print double quotes using escape character #
print("I\"m using double quotes with escape character")

# Add two strings together with a space in between.
# Please note that we have used print(id..) below to know the address of the variable
# As the strings in python are immutable, so the id's are different even if the
# names are same.
market_message = "The market price is:"
print(id(market_message))
market_price = "$100"
market_message = market_message + " " + market_price
print(market_price)
print(id(market_message))

# Get an indexed value out of a string.
# Please note that index values always starts with value 0 and not 1.
# The backward index values starts with -1 and so on.
index_message = "Interstellar"
print(index_message[0])         # This will print the first element of the string
print(index_message[5])         # This will print the 6th element of the string
print(index_message[-1])        # This will print the last element of the string
print(index_message[-4])        # This will print the 4th last element of the string
print(index_message[1:3])       # This will print the characters between 1st and 3rd
                                # element. In this case the 3rd element will not be
                                # printed.
print(index_message[-1:-2])     # This will not print anything. For this we need one
                                # more parameter as third parameter, which is step size
print(index_message[-2:-3:-1])  # This will print one character which will start
                                # with 2nd chracter from last and goes upto 3rd
                                # character from last with a step size of -1.
                                # So in this case it will only print 'a'
print(index_message[-2:1:-1])   # This will print all the characters from back starting
                                # with 2nd character from last and all the way till
                                # 1st character.
print(index_message[-2:1:-2])   # This will start printing from 2nd character from last
                                # with a step size of -2. That means that it will only
                                # print alternate letters from last till 1st item.

# This is to print the statements using f strings and tab delimiter
current_stock_price = 100
last_year_stock_price = 95
print(f"Current year stock price: \t{current_stock_price} \n"
      f"Last year stock price: \t\t{last_year_stock_price}")




