import customer
import receipt

def main():
    # getting the customer data
    name, food, quantity, price, delivery_charges = customer.get_customer()
    
    # to print out the food receipt
    receipt.print_receipt(name, food, quantity, price, delivery_charges)

if __name__ == "__main__":
    main()
