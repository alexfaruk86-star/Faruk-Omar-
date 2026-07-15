def get_customer():
    print("=== Customer Information ===")
    
    # missing input
    name = input("Customer Name : ")
    food = input("Food Ordered (Cake/Muffin) : ")
    quantity = int(input("Quantity : "))
    price = float(input("Price per Item (RM): "))
    delivery_choice = input("Delivery (Y/N): ").upper()
    
    # missing code logic if-else statement
    if delivery_choice == "Y":
        delivery_charges = 5.00
    else:
        delivery_charges = 0.00
        
    return name, food, quantity, price, delivery_charges
