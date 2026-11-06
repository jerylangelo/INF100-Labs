from product import Product

class Inventory:
    def __init__(self):
        #list containing Product objects
        self.products: list[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product_id: str):
        product_to_remove = self.find_product(product_id)
        if product_to_remove:
            self.products.remove(product_to_remove)
            print(f"Product with ID {product_id} removed from inventory.")
        else:
            print(f"Product with ID {product_id} not found in inventory.")

    def find_product(self, product_id: str):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
    
    def display_all(self):
        if not self.products:
            print("Inventory is empty.")
            return
        for product in self.products:
            product.display_information()


