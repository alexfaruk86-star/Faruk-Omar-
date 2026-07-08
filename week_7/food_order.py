def calculate_total(price, quantity):
    # Validate price
    if price <= 0:
        return "invalid price"
    
    # Validate quantity
    if quantity <= 0:
        return "invalid quantity"
    
    # Calculate and return total
    return price * quantity
