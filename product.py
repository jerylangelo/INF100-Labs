from abc import ABC, abstractmethod

from Supplier import Supplier
class Product(ABC): 
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.supplier: Supplier = supplier #supplier object reference

    def update_stock(self, quantity: int) -> None:
        self._stock += quantity
        if self._stock < 0:
            self._stock = 0


    def display_information(self) -> None:
        print(f"ID: {self.product_id} | Name: {self.name} | Price: ${self.price:.2f} | Stock: {self.stock}", end=" ")
        print(f"Supplier: {self.supplier.name} (Contact: {self.supplier.contact_email})")
    @abstractmethod
    def get_fulfillment_info(self) -> str:
        pass
