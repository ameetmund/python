# Reverse a string
# My name is Ameet
# Reverse string should be 'teemA si eman yM'

name = "My name is Ameet"
print(name[::-1])

def rev_str(name):
    rev_name = ''
    for i in name:
        rev_name = i + rev_name
    print(rev_name)

rev_str(name)

