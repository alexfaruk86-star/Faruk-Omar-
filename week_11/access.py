def check_access(is_registered, is_open, is_available):
    if (is_registered.upper() == 'Y' and 
        is_open.upper() == 'Y' and 
        is_available.upper() == 'Y'):
        return "Access Granted"
    else:
        return "Access Denied"


def get_reason(is_registered, is_open, is_available):
    if is_registered.upper() != 'Y':
        return "Student is not registered"
    elif is_open.upper() != 'Y':
        return "Computer lab is closed"
    elif is_available.upper() != 'Y':
        return "No available computer"
    else:
        return "Welcome to the lab."
