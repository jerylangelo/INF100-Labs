import os 

#Tax Rate used for calculation
TAX_RATE = 0.10 
MAX_STORAGE_LIMIT = 500
orders = []  # Initialize orders list to store inventory data
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ORDERS_FILE = os.path.join(BASE_DIR, "inventory.txt")

def load_inventory(): #Load inventory from file
    if not os.path.exists(ORDERS_FILE):
        return []  # If the file doesn't exist, return an empty list

    orders = []

    try:
        with open(ORDERS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = [p.strip() for p in line.split(",")]
                    if len(parts) == 3:
                        order_id = int(parts[0])
                        product_name = parts[1]
                        quantity = int(parts[2])
                        orders.append({
                            "id": order_id,
                            "name": product_name,
                            "qty": quantity
                        })
    except (ValueError, IOError):
        # Handle corrupted file gracefully by returning what was parsed so far
        pass

    return orders
def save_inventory(inventory):
    try:
        with open(ORDERS_FILE, "w") as f:
            for order in inventory:
                f.write(f"{order['id']}, {order['name']}, {order['qty']}\n")
        print(f"\nOrder successfully saved to {ORDERS_FILE}")
    except IOError as e:
        print(f"\n[ERROR] Failed to save orders: {e}")
def get_valid_input():
    """
    Prompts user for product name and quantity.
    Returns (product_name, quantity) tuple or ('quit', None) to exit.
    """
    name_input = input("Enter Product Name: ").strip()
    if name_input.lower() == 'quit':
        return 'quit', None

    while True:
        qty_input = input("Enter Quantity: ").strip()
        if qty_input.lower() == 'quit':
            return 'quit', None
        
        try:
            quantity = int(qty_input)
            if quantity > 0:
                return name_input, quantity
            else:
                print("Quantity must be a positive integer. Try again.")
        except ValueError:
            print("Invalid quantity! Please enter a valid integer.")
def display_current_orders():
    if not orders:
        print("\nNo current orders.")
        return

    print("\nCurrent Orders:")
    for order in orders:
        print(f"ID: {order['id']}, Product: {order['name']}, Quantity: {order['qty']}")
        print()

def main():
    orders = load_inventory()  # Load existing orders from file

    while True:
        product_name, quantity = get_valid_input()
        if product_name == 'quit':
            break

        new_order = {
            "id": len(orders) + 1,
            "name": product_name,
            "qty": quantity
        }

        orders.append(new_order)
        print(f"\nOrder added: ID: {new_order['id']}, Product: {new_order['name']}, Quantity: {new_order['qty']}")
        
        
        

    save_inventory(orders)

    
        
   

if __name__ == "__main__":
    main()

    
    
        


