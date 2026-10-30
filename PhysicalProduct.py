from product import Product
from CanBeShipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock) #This line calls the constructor of the parent class Product to initialize the common attributes.
        
        self.weight = weight # This initializes the weight attribute specific to PhysicalProduct.

    def display_information(self):
        super().display_information() #Calls the display_information method of the parent class Product.
        print(f"| Weight: {self.weight} kg") #Print weight of PhysicalProduct
            

    def get_fulfillment_info(self):
        return "This product requires physical shipping." #implement abstract method from product class.

    def calculate_shipping_cost(self):
        #implementing interface rule
        return 5.0 + (self.weight * 2.0)