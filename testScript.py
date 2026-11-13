import unittest
from DiscountStrategy import DiscountStrategy
from PercentageDiscount import PercentageDiscount
from BulkDiscount import BulkDiscount
from NoDiscount import NoDiscount
from StudentDiscount import StudentDiscount
from ProductFactory import ProductFactory
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier
from inventory import Inventory
from Order import Order
from OrderLine import OrderLine
from inventory_manager import load_products

def run_all_lab9_tests() -> None:

    print("Lab 9 Tests:")
    supplier = Supplier("SUP-001", "Tech Corp", "support@techcorp.com")

    # 1. Test Strategy Pattern
    print("\n 1. Testing Strategy Pattern & Discounts ")
    no_disc = NoDiscount()
    assert no_disc.apply(250.0) == 250.0, "NoDiscount failed"
    print("[PASS] NoDiscount calculation correct.")

    pct_disc = PercentageDiscount(10)  # 10% off
    assert pct_disc.apply(200.0) == 180.0, "PercentageDiscount failed"
    print("[PASS] PercentageDiscount calculation correct.")

    bulk_disc = BulkDiscount(200.0, 20.0)
    assert bulk_disc.apply(250.0) == 230.0, "BulkDiscount (meets threshold) failed"
    assert bulk_disc.apply(150.0) == 150.0, "BulkDiscount (below threshold) failed"
    print("[PASS] BulkDiscount calculations correct.")

    student_disc = StudentDiscount(5.0)  # 5% off
    assert student_disc.apply(100.0) == 95.0, "StudentDiscount failed"
    print("[PASS] StudentDiscount calculation correct.")

    # 2. Test Order with Strategy Delegation & Dynamic Change
    print("\n 2. Testing Order Strategy Delegation ")
    product = ProductFactory.create("physical", "P001", "Lamp", 100.0, 10, supplier, 2.0)
    order = Order("ORD-001", BulkDiscount(200.0, 20.0))
    order.add_order_line(product, 3)  # Total = 300.0
    
    # Initial bulk discount (300 - 20 = 280)
    assert order.calculate_total() == 280.0, "Order bulk discount total failed"
    print("[PASS] Order successfully calculated total using BulkDiscount ($280.0).")

    # Dynamic strategy change
    order.set_discount(PercentageDiscount(10))  # 10% off 300 = 270
    assert order.calculate_total() == 270.0, "Order dynamic strategy change failed"
    print("[PASS] Order successfully switched strategy via set_discount() ($270.0).")

    # 3. Test Factory Pattern
    print("\n 3. Testing ProductFactory ")
    physical = ProductFactory.create("physical", "P002", "Desk", 150.0, 5, supplier, 12.0)
    digital = ProductFactory.create("digital", "D001", "E-Book", 30.0, 100, supplier, 15.0)
    
    assert isinstance(physical, PhysicalProduct), "Factory did not create PhysicalProduct"
    assert isinstance(digital, DigitalProduct), "Factory did not create DigitalProduct"
    print("[PASS] ProductFactory successfully created physical and digital products.")

    # Test factory unknown type error
    try:
        ProductFactory.create("service", "S001", "Consulting", 100.0, 1, supplier)
        raise AssertionError("Factory should have raised ValueError for unknown type")
    except ValueError as e:
        print(f"[PASS] Factory correctly raised ValueError for unknown type: {e}")

    # 4. Test Class-Level Validation Rules
    print("\n 4. Testing Validation Rules ")
    # Invalid price <= 0
    try:
        ProductFactory.create("physical", "P999", "Bad Item", -10.0, 5, supplier, 1.0)
        raise AssertionError("Should have failed validation for negative price")
    except ValueError as e:
        print(f"[PASS] Validation caught invalid price: {e}")

    # Invalid stock < 0
    try:
        ProductFactory.create("physical", "P998", "Bad Item 2", 50.0, -2, supplier, 1.0)
        raise AssertionError("Should have failed validation for negative stock")
    except ValueError as e:
        print(f"[PASS] Validation caught invalid stock: {e}")

    # Invalid OrderLine quantity <= 0
    chair = ProductFactory.create("physical", "P003", "Chair", 50.0, 10, supplier, 5.0)
    try:
        OrderLine("ORD-999", chair, 0)
        raise AssertionError("Should have failed validation for zero quantity order line")
    except ValueError as e:
        print(f"[PASS] Validation caught invalid OrderLine quantity: {e}")

    # 5. Test File Loading and Exception Handling (Section 5.2 & 7)
    print("\n 5. Testing File Loading & Error Handling ")
    test_inventory = Inventory()
    
    # Test missing file handling (should print message and not crash)
    print("Testing missing file :")
    load_products("non_existent_file.csv", test_inventory, supplier)

    # Test loading actual products.csv (ensure it loads valid rows and skips bad ones)
    print("Testing valid/malformed rows from products.csv:")
    load_products("products.csv", test_inventory, supplier)
    assert len(test_inventory.products) > 0, "Inventory failed to load valid products from CSV"
    print(f"[PASS] Successfully loaded {len(test_inventory.products)} valid products while handling exceptions.")

    print("All tests passed")

if __name__ == "__main__":
    run_all_lab9_tests()