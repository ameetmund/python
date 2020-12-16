# Builtin functions that we can use on strings
# Highly used builtin functions - len(), id(), type(),
# Highly used builtin methods upper(), lower() strip(), find(), split()
# join(), capitalize()
# Refer https://docs.python.org/3/library/functions.html for details.

# Following is the way of importing a python library or functions
import string
from string import capwords


message = "Hello Ameet How are you?"
message1 = "Hello-Ameet-How-are-you?"
message2 = ["Very", "Good", "Morning"]
# Builtin functions
print(len(message))     # This will give the length of the string
print(id(message))      # This will give the storage id of the string
print(type(message))    # This will give the data type of the variable like int or string etc...

# Builtin methods
# There is a difference between usage of builtin functions and methods.
# Methods can't be directly used like function. This must be used by typing '.' after
# any variable to do a certain operation on that.
print(message.upper())  # To convert all the characters to upper characters
print(message.lower())  # To convert all the characters to lower characters
print(message.strip())  # To strip all the unwanted extra spaces between words
print(message.strip("?"))  # To strip unwanted characters present in the variable
print(message.find("How")) # This will give the position of a partition word or char
print(message.find("Good")) # This will result in -1 as the value is not present
print(message.find("How", 10, 20)) # This will give the result based on the starting and end length
print(message.split())  # This will split the string into words. By default it uses space for split
print(message1.split("-"))  # This uses '-' to split the string.
print(" ".join(message2))   # This will join the words using space and make a statement
print("-".join(message2))   # This will join the words using '-' and make a statement.
print(message.capitalize())    # This will only make the first letter of the string as capital

lower = string.ascii_lowercase
print(lower)   # This will get the lower case values

upper = string.ascii_uppercase
print(upper)    # This will get the upper case value

print(capwords(message))    # This will make all the first letters as capital


