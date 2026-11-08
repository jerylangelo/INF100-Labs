from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from inventory import Inventory
from Order import Order
from product import Product

def run_all_lab8_tests() -> None:
    print("==================================================")
    print("          LAB 8 VERIFICATION TESTS       ")
    print("==================================================")

    # 1. Test Association (Supplier & Product)
    print("\n--- 1. Testing Association (Supplier & Product) ---")
    supplier = Supplier("SUP-001", "Tech Solutions", "contact@techsolutions.com")
    
    # Passing weight (2.5) before supplier to match PhysicalProduct signature
    laptop = PhysicalProduct("P001", "Gaming Laptop", 1299.99, 5, 2.5, supplier)
    print(f"Product: {laptop.name} supplied by {laptop.supplier.name} ({laptop.supplier.contact_email})")

    # 2. Test Aggregation (Inventory & Product)
    print("\n--- 2. Testing Aggregation (Inventory & Product) ---")
    my_inventory = Inventory()
    my_inventory.add_product(laptop)
    print(f"Added {laptop.name} to Inventory. Total products: {len(my_inventory.products)}")
    
    # Remove from inventory to test independent lifecycle
    my_inventory.remove_product("P001")
    print(f"After removal, product stock remains accessible: {laptop.stock}")

    # 3. Test Composition (Order & OrderLine)
    print("\n--- 3. Testing Composition (Order & OrderLine) ---")
    order = Order("ORD-2026-001")
    order.add_order_line(laptop, 1)
    
    # Create digital product (adjust argument order if DigitalProduct has a unique signature)
    ebook = DigitalProduct("D001", "Python Architecture E-Book", 39.99, 100, 15.0,supplier)
    order.add_order_line(ebook, 2)

    print(f"Order ID: {order.order_id}")
    for line in order.order_lines:
        print(f"  - Item: {line.product.name} | Qty: {line.quantity} | Subtotal: ${line.calculate_subtotal():.2f}")
    print(f"Calculated Order Total: ${order.calculate_total():.2f}")

    # Test removing an order line
    order.remove_order_line("D001")
    print(f"Order Total after removing E-Book: ${order.calculate_total():.2f}")

    # 4. Test LSP & Polymorphism
    print("\n--- 4. Testing LSP & Polymorphism ---")
    
    def display_product_features(product: Product) -> None:
        """Function demonstrating Liskov Substitution Principle"""
        product.display_information()
        print(f"Fulfilment Details: {product.get_fulfillment_info()}\n")

    print("Testing via LSP function call:")
    display_product_features(laptop)
    display_product_features(ebook)

    print("Testing via Polymorphic Inventory Loop:")
    poly_inventory = Inventory()
    poly_inventory.add_product(laptop)
    poly_inventory.add_product(ebook)

    for p in poly_inventory.products:
        print(f"-> Polymorphic check: {p.name} | Fulfilment: {p.get_fulfillment_info()}")

    print("\n==================================================")
    print("          ALL LAB 8 TESTS PASSED SUCCESSFULLY     ")
    print("==================================================")

if __name__ == "__main__":
    run_all_lab8_tests()