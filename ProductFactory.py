from product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier

class ProductFactory:
    """Factory class to centralise product creation."""

    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float, 
               stock: int, supplier: Supplier, weight: float = 0.0, file_size: float = 0.0) -> Product:
       
        if product_type == "physical":
            # Adjust parameter order if your PhysicalProduct constructor differs
            return PhysicalProduct(product_id, name, price, stock, weight, supplier)
        elif product_type == "digital":
            # Adjust parameter order if your DigitalProduct constructor differs
            return DigitalProduct(product_id, name, price, stock, file_size, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")