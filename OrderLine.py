
from product import Product


class OrderLine: 
    def __init__(self, order_id: str, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("OrderLine quantity must be greater than zero.")
        
        self.order_id: str = order_id
        self.product: Product = product
        self.quantity: int = quantity
    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity
        