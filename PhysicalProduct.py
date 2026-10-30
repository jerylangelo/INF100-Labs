from product import Product
from inventory import Inventory

class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock) #This line calls the constructor of the parent class Product to initialize the common attributes.
        
        self.weight = weight # This initializes the weight attribute specific to PhysicalProduct.

        def display_information(self):
            super().display_information() #Calls the display_information method of the parent class Product.
            print(f"Weight: {self.weight} kg") #Print weight of PhysicalProduct
            

