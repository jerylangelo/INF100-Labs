
from Order import Order
from PhysicalProduct import PhysicalProduct
from Supplier import Supplier


def test_composition():
    print("\n--- Testing Composition (Section 4.3) ---")
    
    # 1. Create independent objects (Supplier and Products)
    supplier = Supplier("SUP-001", "Tech Supplies", "tech@supplies.com")
    laptop = PhysicalProduct("P001", "Laptop", 999.99, 10, supplier, 2.5)
    mouse = PhysicalProduct("P002", "Wireless Mouse", 25.00, 50, supplier, 0.2)

    # 2. Create Order 1 and add products using add_order_line()
    order1 = Order("ORD-001")
    order1.add_order_line(laptop, 1)
    order1.add_order_line(mouse, 2)

    print(f"Order ID: {order1.order_id}")
    for line in order1.order_lines:
        print(f"  - {line.product.name} (Qty: {line.quantity}) | Subtotal: ${line.calculate_subtotal():.2f}")
    print(f"Total Order Value: ${order1.calculate_total():.2f}\n")

    # 3. Add the same Product to a different Order (Order 2)
    order2 = Order("ORD-002")
    order2.add_order_line(laptop, 1) # Adding the same laptop product again

    print(f"Order ID: {order2.order_id}")
    for line in order2.order_lines:
        print(f"  - {line.product.name} (Qty: {line.quantity}) | Subtotal: ${line.calculate_subtotal():.2f}")
    print(f"Total Order Value: ${order2.calculate_total():.2f}\n")

    # 4. Verify object identity 
    line_in_order1 = order1.order_lines[0]
    line_in_order2 = order2.order_lines[0]

    print("--- Verification Check ---")
    print(f"Are the OrderLine objects the same? {line_in_order1 is line_in_order2}") 
    # Expected: False (Each Order creates and owns its own separate OrderLine objects)
    
    print(f"Are the Product objects inside the OrderLines the same? {line_in_order1.product is line_in_order2.product}") 
    # Expected: True (The independent Product object is referenced by both lines)


    # Test removing an order line
    print("\n--- Testing Order Line Removal ---")
    print(f"Total before removal: ${order1.calculate_total():.2f}")
    
    # Remove the laptop line using the Order's own method
    order1.remove_order_line("P001") 
    
    print(f"Total after removal: ${order1.calculate_total():.2f}")
test_composition()
