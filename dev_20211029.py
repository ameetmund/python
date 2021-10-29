# Reverse a string
# My name is Ameet
# Reverse string should be 'teemA si eman yM'

name = "My name is Ameet"
print(name[::-1])

def rev_str(name):
    rev_list = []
    for i, j in enumerate(name):
        print(i, j)
        if i <= len(name)-1:
            rev_list.append(j)
        else:
            break
    rev_name = ''.join(rev_list[::-1])
    print(rev_name)

rev_str(name)

