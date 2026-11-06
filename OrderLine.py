
from product import Product


class OrderLine: 
    def __init__(self, order_id: str, product: Product, quantity: int) -> None:
        self.order_id: str = order_id
        self.product: Product = product
        self.quantity: int = quantity
    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity
        