from product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def search_product(self, product_id: str):
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


