from class_getter_setter import Laptop

class Dealer(Laptop):
    def __init__(self):
        print("Get all the init variables from main class")
        super().__init__()
    
    def get_geo_location(self):
        print("Get the same geo from main class")
        super().get_geo()

if __name__ == '__main__':
    dealer = Dealer()
    dealer.get_geo_location()
    
