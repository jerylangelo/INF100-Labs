#Tax Rate used for calculation
TAX_RATE = 0.10 



def get_valid_input(): #Handles the prompt, handles input validation, and returns a valid integer or a "quit" signal.
    user_input = input("Enter stock quantity (or 'quit' to exit): ").strip()
    
    # Check for exit command
    if user_input.lower() == "quit":
        return 'quit'

    try:
        value = int(user_input)
        if value < 0:
            return None #Values cannot be a negative number
        return value
    except ValueError:
        return None #Cannot be non integer values
def calculate_tax(amount): #Calculate Tax
    value = amount * TAX_RATE
    return value 
def process_delivery(current_total,new_value): #Calculate new value
    if current_total > 500:
         print("\nALERT: Storage capacity exceeded! Overstock limit of 500 reached.")
         return current_total
    return current_total + new_value
def generate_report(total_units, total_tax, successful_deliveries, failed_attempts):
    #Reporting summary on termination
    print("\n--- Daily Audit Report ---")
    print(f"Total Units Processed: {total_units}")
    print(f"Total Tax Calculated:  {total_tax}")
    print(f"Successful Deliveries: {successful_deliveries}")
    print(f"Failed/Rejected Entries: {failed_attempts}")
def main():
    current_total = 0
    total_tax = 0.0
    successful_deliveries = 0
    failed_attempts = 0 

    while True:
        result = get_valid_input()

        if result == 'quit' :
            break
        elif result is None:
            failed_attempts += 1
            print("Invalid entry. Please enter a non-negative integer or 'quit'! ")
        else:
            delivery_tax = calculate_tax(result)
            current_total = process_delivery(current_total, result)
            total_tax += delivery_tax
            successful_deliveries += 1
            print(f"Logged Delivery: {result} units | Delivery Tax: {delivery_tax:.2f} | Total : {current_total}")
    generate_report(current_total, total_tax, successful_deliveries,failed_attempts)

if __name__ == "__main__":
    main()

    
    
        


