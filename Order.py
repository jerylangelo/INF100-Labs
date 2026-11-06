from OrderLine import OrderLine
from product import Product     


class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

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


    def calculate_total(self) -> float:
        total = 0.0
        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()
        return total
    