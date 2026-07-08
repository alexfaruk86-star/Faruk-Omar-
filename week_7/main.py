# Import the function from food_order.py
from food_order import calculate_total

def main():
    try:
        price = float(input("Price (RM): "))
        quantity = int(input("Quantity: "))
        
        # Call the imported function
        total = calculate_total(price, quantity)
        
        # Check if validation failed or calculation succeeded
        if isinstance(total, str):
            print(f"Error: {total}")
        else:
            print(f"Total Payment = RM {total:.2f}")
            
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()
