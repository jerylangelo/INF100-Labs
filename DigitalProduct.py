from product import Product

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, file_size: float):
        super().__init__(product_id, name, price, stock)  # Call the constructor of the parent class Product to initialize common attributes.
        
        self.file_size = file_size  # Initialize the file_size attribute specific to DigitalProduct.


    def display_information(self):
        super().display_information()  # Call the display_information method of the parent class Product.
        print(f"| Download Size: {self.file_size} MB")  # Print file size of DigitalProduct