# TODO 
# Class is something that defines a particular entity/group
class Laptop:
    "Defines variety of laptops"
    # laptop_type = " "
    # laptop_brand = " "
    # laptop_model = " "

    # Constructor - 
    def __init__(self):
        self.laptop_type = "Windows"
        self.laptop_brand = "Lenevo"
        self.laptop_model = "Ideapad"
    
    # Printing
    def print_constructor(self):
        print(self.laptop_type, self.laptop_brand, self.laptop_model)

    
laptop = Laptop()
# laptop.laptop_brand = "Lenevo"
# laptop.laptop_type = "Windows"
# laptop.laptop_model = "Ideapad"

laptop.print_constructor()





