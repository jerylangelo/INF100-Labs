import os 
import json
#Weekly Lab 5

inventory = [
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40
    },
    {
        "id": "P003",
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25
    }
]
def display_all():
    global inventory
    print("\nCurrent Inventory:")
    print("-"*50)

    for product in inventory:
        print(
            f"ID:{product['id']} | "
            f"Name:{product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock:{product['stock']}"
        )
    print("-"*50)

def add_product():
    print("\nAdd New Product")
    product_id = input("Enter Product ID: ")
    product_name = input("Enter Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock
        
    }
    inventory.append(product)
    print(f"Product {product_name} added successfully!")

def update_stock():
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found:")
            print(f":Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")

            new_stock = int(input("Enter New Stock Quantity: "))
            product["stock"] = new_stock
            print(f"Stock for {product['name']} updated to {new_stock}.")

            return
    print("Product not found.")

def search_product():
    print("\nSearch Product")

    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found:")
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            return
    print("Product not found.")

def load_inventory():
    global inventory
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
        print("Inventory loaded successfully.")    
            
    else:
        print("No existing inventory found. Starting with default inventory.")
        return []
def save_inventory():
    global inventory
    print("Saving inventory...")
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

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
            display_all()
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


                
load_inventory()
menu()
