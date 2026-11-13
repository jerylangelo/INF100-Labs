from OrderLine import OrderLine
from product import Product     
from DiscountStrategy import DiscountStrategy


class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy = None) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        self.discount: DiscountStrategy = discount if discount is not None else None

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(self.order_id, product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> None:
        for order_line in self.order_lines:
            if order_line.product.product_id == product_id:
                self.order_lines.remove(order_line)
                print(f"Order line from product ID {product_id} removed from order {self.order_id}.")
                break
        print(f"Product with ID {product_id} not found in order {self.order_id}.")
        return

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total) 

        
    