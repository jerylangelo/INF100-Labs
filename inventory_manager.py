import os 
import json
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier
from product import Product
from inventory import Inventory

#Weekly Lab 8
inventory = Inventory()

FILENAME = "inventory.json"

def add_product():
    #Product details
    print("\nAdd New Product")
    p_type = input("Enter product type ('p' for Physical, or 'd' for digital): ").strip().lower()
    product_id = input("Enter Product ID: ")
    product_name = input("Enter Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    #Supplier details
    print("\nEnter Supplier Details:")
    sup_id = input("Enter Supplier ID: ")
    sup_name = input("Enter Supplier Name: ")
    sup_email = input("Enter Supplier Email: ")
    product_supplier = Supplier(sup_id, sup_name, sup_email)

    if p_type == 'p':
        weight = float(input("Enter Weight (kg): " ))
        new_product = PhysicalProduct(product_id, product_name, price, stock, weight, product_supplier)
    elif p_type == "d":
        download_size = float(input("Enter download size (MB): "))
        new_product = DigitalProduct(product_id, product_name, price, stock, download_size, product_supplier)
    else:
        print("Invalid product type selected. Product not added")
        return
    
    inventory.add_product(new_product)
    print(f"Product {product_name} added successfully!")

def update_stock():
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
    if product:
        product.display_information()
        new_stock = int(input("Enter New Stock Quantity: "))
        product.stock = new_stock
        print(f"Stock for {product.name} updated to {new_stock}.")
    else:
        print("Product not found.")

def search_product():
    print("\nSearch Product")

    product_id = input("Enter Product ID: ")

    product = inventory.search_product(product_id)
    if product:
        product.display_information()
    else:
        print("Product not found.")

def load_inventory():
     # Create a default supplier for the default items
    default_supplier = Supplier("SUP-001", "Default Tech Corp", "contact@defaulttech.com")
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        print("No existing inventory found. Loading default inventory.")
        # Default starting inventory with both types
        inventory.add_product(PhysicalProduct("P001", "Laptop", 999.99, 10, 2.5, default_supplier))
        inventory.add_product(DigitalProduct("P002", "Antivirus Software", 45.00, 25, 150.0, default_supplier))
        return

    with open(FILENAME, "r") as file:
        data = json.load(file)

    for item in data:
        # Recreate the Supplier object using the saved dictionary keys
        if "supplier_id" in item:
            prod_supplier = Supplier(
                item["supplier_id"], 
                item["supplier_name"], 
                item["supplier_email"]
            )
        else:
            prod_supplier = default_supplier
        if item.get("type") == "physical":
            prod = PhysicalProduct(
                product_id=item["id"],
                name=item["name"],
                price=item["price"],
                stock=item["stock"],
                weight=item["weight"],
                supplier=prod_supplier
            )
        elif item.get("type") == "digital":
            prod = DigitalProduct(
                product_id=item["id"],
                name=item["name"],
                price=item["price"],
                stock=item["stock"],
                file_size=item["download_size"],
                supplier=prod_supplier
            )
        else:
            continue
        inventory.add_product(prod)
    print("Inventory loaded successfully.")

def save_inventory():
    data = []
    for product in inventory.products:
        item = {
            "id": product.product_id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock,
            "supplier_id": product.supplier.supplier_id,
            "supplier_name": product.supplier.name,
            "supplier_email": product.supplier.contact_email
        }
        if isinstance(product, PhysicalProduct):
            item["type"] = "physical"
            item["weight"] = product.weight
        elif isinstance(product, DigitalProduct):
            item["type"] = "digital"
            item["download_size"] = product.file_size
        data.append(item)

    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully to inventory.json.")

def menu():
    while True: 
        print("\n----------MENU----------")
        print("1. Display All Products")
        print("2. Add New Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Exit")
        print("--------------------------")

        choice = input("Enter option: ")

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            search_product()
        elif choice == "5":
            print("Saving inventory before exit...")
            save_inventory()
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break    
        else:
            print("Invalid option. Please try again.")


                
if __name__ == "__main__":
    

    load_inventory()
    menu()
    