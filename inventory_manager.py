import os 
import json
from PhysicalProduct import PhysicalProduct
from product import Product
from inventory import Inventory
#Weekly Lab 8
inventory = Inventory()


def add_product():
    print("\nAdd New Product")
    product_id = input("Enter Product ID: ")
    product_name = input("Enter Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    new_product = Product(product_id=product_id, name=product_name, price=price, stock=stock)
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
    if not os.path.exists("inventory.json"):
        print("No existing inventory found. Starting with default inventory.")
    elif os.path.getsize("inventory.json") == 0:
        print("Inventory file is empty. Starting with default inventory.")
    else:
        with open("inventory.json", "r") as file:
            data = list(json.load(file))
        for item in data:
            prod = Product(
                product_id=item["id"],
                name=item["name"],
                price=item["price"],
                stock=item["stock"]
            )
            inventory.add_product(prod)
        print("Inventory loaded successfully.")
        return

    # Default inventory
    inventory.add_product(Product("P001", "Laptop", 999.99, 10))
    inventory.add_product(Product("P002", "Mouse", 25.50, 40))
    inventory.add_product(Product("P003", "Keyboard", 45.00, 25))

def save_inventory():
    data = [
        {
            "id": product.product_id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock
        }
        for product in inventory.products
    ]

    with open("inventory.json", "w") as file:
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
    