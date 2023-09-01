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
    
    # Getter
    # Note that the laptop_geo has 2 underscores before it
    # This will make the variable private and no one can
    # change the value of
    def get_geo(self):
        self.__laptop_geo = "India"
        return self.__laptop_geo

    # Setter 
    def set_geo(self, laptop_geo):
        self.__laptop_geo = laptop_geo
    
    # Printing
    def print_constructor(self):
        print(self.laptop_type, self.laptop_brand, self.laptop_model)

    
laptop = Laptop()
# laptop.laptop_brand = "Lenevo"
# laptop.laptop_type = "Windows"
# laptop.laptop_model = "Ideapad"

# laptop.print_constructor()



print(laptop.get_geo())
laptop.set_geo("Europe")
print(laptop.___laptop_geo)







