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

    product_id = ("Enter Product ID: ")

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


