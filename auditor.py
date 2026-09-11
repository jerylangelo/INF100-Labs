
#Initialize tracking variables
inventory_total = 0
failed_entries_count = 0

#Run a continuous loop until the user types 'quit' or triggers an alert
while True:
    user_input = input("Enter stock quantity (or 'quit' to exit): ").strip()
    
    # Check for exit command
    if user_input.lower() == "quit":
        break
    
    #Validate numeric input using .isdigit()
    if not user_input.isdigit():
        print("Error: Invalid input. Please enter a positive whole number.")
        failed_entries_count += 1
        continue
    
    #Convert to integer and enforce business rules (non-negative)
    quantity = int(user_input)
    
    if quantity < 0:
        print("Error: Negative values are rejected.")
        failed_entries_count += 1
        continue
    
    #Manage State - Update running total
    inventory_total += quantity
    print(f"Accepted {quantity} units. Current inventory: {inventory_total}")
    
    #Trigger Overstock Alert if total exceeds 500 units
    if inventory_total > 500:
        print("\nALERT: Storage capacity exceeded! Overstock limit of 500 reached.")
        break

#Reporting summary on termination
print("\n--- Daily Audit Report ---")
print(f"Total Units Processed : {inventory_total}")
print(f"Failed/Rejected Entries: {failed_entries_count}")