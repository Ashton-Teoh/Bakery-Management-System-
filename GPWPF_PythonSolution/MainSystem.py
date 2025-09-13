STAFF_LIST_FILE = 'staff_list.txt'


def read_file(file_name):
    """Reads data from a file and returns it as a list of lines."""
    try:
        with open(file_name, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def write_file(file_name, data, mode='a'):
    """Writes data to a file."""
    with open(file_name, mode) as file:
        file.write(data + '\n')

# Staff Login
def staff_login():
    staff_list = read_file(STAFF_LIST_FILE)
    while True:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        for line in staff_list:
            stored_username, stored_password = line.strip().split(',')
            if stored_username == username and stored_password == password:
                print(f"Welcome, {username}!")
                return True
        print("Invalid username or password. Please try again.")

# Main menu for staff roles
def staff_menu():
    while True:
        print("\n--- Staff Menu ---")
        print("1. Manager")
        print("2. Cashier")
        print("3. Baker")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            import manager
            print("Opening Manager Menu...")
            manager.main_menu()

        elif choice == '2':
            import cashier
            print("Opening Cashier Menu...")
            cashier.maincashier()

        elif choice == '3':
            import baker
            print("Opening Baker Menu...")
            baker.mainbaker()

        elif choice == '4':
            print("Logging out...")
            break
        
        else:
            print("Invalid choice! Please try again.")

# Customer functions
def customer_menu():
    import customer
    print("Opening Customer Menu...")
    customer.maincustomer()

def main():
    while True:
        print("\n--- Welcome to the Bakery Management System ---")
        print("Are you a:")
        print("1. Staff")
        print("2. Customer")
        print("3. Exit")
        user_type = input("Enter your choice: ")

        if user_type == '1':
            if staff_login():
                staff_menu()
        elif user_type == '2':
            customer_menu()
        elif user_type == '3':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the program
main()
