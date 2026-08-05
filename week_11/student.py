def get_student():
    print("====== Computer Lab Access ======")
    name = input("Student Name : ")
    student_id = input("Student ID   : ")
    is_registered = input("Registered for today's lab? (Y/N): ")
    is_open = input("Is the lab open? (Y/N): ")
    is_available = input("Computer Available? (Y/N): ")
    
    return name, student_id, is_registered, is_open, is_available
