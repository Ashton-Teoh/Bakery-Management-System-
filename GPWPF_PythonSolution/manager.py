# Store user data in a dictionary
user = {}
order = {}
inventory = {}
cusfeedback = []

# Function to load user data from a text file
def load_users():
    try:
        with open("users.txt", "r") as f:
            for line in f:
                username, password = line.strip().split(",")
                user[username] = password
    except FileNotFoundError:
        print("User data file not found, creating a new one...")

# Function to save user data to a text file
def save_users():
    with open("users.txt", "w") as f:
        for username, password in user.items():
            f.write(f"{username},{password}\n")

# Function to add a user
def add_user(username, password):
    if username not in user:
        user[username] = password
        save_users()
        print("User " + username + " added successfully.")
    else:
        print("User " + username + " already exists.")

# Function to remove a user
def remove_user(username):
    if username in user:
        del user[username]
        save_users()
        print("User " + username + " removed.")
    else:
        print("User " + username + " does not exist.")

# Function to update a user's password
def update_password(username, newpassword):
    if username in user:
        user[username] = newpassword
        save_users()
        print("Password for user " + username + " updated.")
    else:
        print("User " + username + " does not exist.")

# Function to display all users
def display_users():
    if user:
        print("Current users:")
        for username in user.keys():
            print("- " + username)
    else:
        print("No users found.")

# Function to load order data from a text file
def load_orders():
    try:
        with open("orders.txt", "r") as f:
            for line in f:
                order_id, status = line.strip().split(",")
                order[order_id] = status
    except FileNotFoundError:
        print("Order data file not found, creating a new one...")

# Function to save order data to a text file
def save_orders():
    with open("orders.txt", "w") as f:
        for order_id, status in order.items():
            f.write(f"{order_id},{status}\n")

# Function to add an order
def add_order(order_id, status="Pending"):
    if order_id not in order:
        order[order_id] = status
        save_orders()
        print("Order " + order_id + " added with status " + status)
    else:
        print("Order already exists.")

# Function to update order status
def update_order(order_id, newstatus):
    if order_id in order:
        order[order_id] = newstatus
        save_orders()
        print("Order: " + order_id + " updated to " + newstatus)
    else:
        print("Order: " + order_id + " not found.")

# Function to view all orders
def order_view():
    if order:
        print("Current Orders:")
        for order_id, status in order.items():
            print("OrderID: " + order_id + " Status: " + status)
    else:
        print("No orders found.")

# Function to load inventory data from a text file
def load_inventory():
    try:
        with open("inventory.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:  # Proceed only if line is not empty
                    try:
                        name, quantity = line.split(",")
                        inventory[name] = int(quantity)
                    except ValueError:
                        print(f"Skipping invalid line in inventory: '{line}'")
    except FileNotFoundError:
        print("Inventory data file not found, creating a new one...")

# Function to save inventory data to a text file
def save_inventory():
    with open("inventory.txt", "w") as f:
        for name, quantity in inventory.items():
            f.write(f"{name},{quantity}\n")

# Function to add or update an inventory item
def add_update_item(name, quantity):
    quantity = int(quantity)
    if name in inventory:
        inventory[name] += quantity
        print(f"Added {quantity} units of {name}.")
    else:
        inventory[name] = quantity
        print(f"Added item {name} with quantity {quantity}.")
    save_inventory()

# Function to remove an item from inventory
def remove_item(name):
    if name in inventory:
        del inventory[name]
        save_inventory()
        print("Removed item " + name)
    else:
        print("Item " + name + " not found.")

# Function to view all inventory items
def view_items():
    if inventory:
        print("Inventory list:")
        for name, quantity in inventory.items():
            print(f"- {name}: Quantity {quantity}")
    else:
        print("No inventory found.")

# Financial management
income = 0
expenses = 0

# Function to load finance data from a file
def load_data():
    global income, expenses
    try:
        with open("finance_data.txt", "r") as file:
            data = file.readlines()
            income = float(data[0].strip())  # Load income
            expenses = float(data[1].strip())  # Load expenses
    except FileNotFoundError:
        print("No previous data found, starting fresh.")

# Function to save finance data to a file
def save_data():
    with open("finance_data.txt", "w") as file:
        file.write(str(income) + "\n")
        file.write(str(expenses) + "\n")

# Function to calculate profit
def cal_profit():
    return income - expenses

# Customer feedback functions
def load_feedback():
    global cusfeedback
    try:
        with open("feedback.txt", "r") as file:
            cusfeedback = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("No previous feedback found, starting fresh.")

def save_feedback():
    with open("feedback.txt", "w") as file:
        for feedback in cusfeedback:
            file.write(feedback + "\n")

def add_feedback(feedback):
    cusfeedback.append(feedback)
    print("Feedback added: " + feedback)
    save_feedback()

def view_feedback():
    if cusfeedback:
        print("Feedbacks:")
        for feedback in cusfeedback:
            print("- " + feedback)
    else:
        print("No feedback")

# Main menu
def main_menu():
    load_users()
    load_orders()
    load_inventory()
    load_data()
    load_feedback()

    while True:
        print("\n--- Bakery Management System ---")
        print("1. User Management")
        print("2. Order Management")
        print("3. Inventory Management")
        print("4. Financial Management")
        print("5. Customer Feedback")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            user_management()
        elif choice == "2":
            order_management()
        elif choice == "3":
            inventory_management()
        elif choice == "4":
            finance_management()
        elif choice == "5":
            feedback_management()
        elif choice == "6":
            print("Exiting the system.")
            break
        else:
            print("Invalid option, please try again.")

# User Management
def user_management():
    while True:
        print("\nUser Management")
        print("1. Add User")
        print("2. Remove User")
        print("3. Update User Password")
        print("4. Display All Users")
        print("5. Back to Main Menu")

        option = input("Enter your choice (1-5): ")

        if option == "1":
            username = input("Enter username to add: ")
            password = input("Enter password: ")
            add_user(username, password)
        elif option == "2":
            username = input("Enter username to remove: ")
            remove_user(username)
        elif option == "3":
            username = input("Enter username: ")
            newpassword = input("Enter new password: ")
            update_password(username, newpassword)
        elif option == "4":
            display_users()
        elif option == "5":
            break
        else:
            print("Invalid option, please try again.")

# Order Management
def order_management():
    while True:
        print("\nOrder Management")
        print("1. Add Order")
        print("2. Update Order Status")
        print("3. View All Orders")
        print("4. Back to Main Menu")

        option = input("Enter your choice (1-4): ")

        if option == "1":
            order_id = input("Enter Order ID: ")
            add_order(order_id)
        elif option == "2":
            order_id = input("Enter Order ID to update: ")
            status = input("Enter new status: ")
            update_order(order_id, status)
        elif option == "3":
            order_view()
        elif option == "4":
            break
        else:
            print("Invalid option, please try again.")

# Inventory Management
def inventory_management():
    while True:
        print("\nInventory Management")
        print("1. Add/Update Item")
        print("2. Remove Item")
        print("3. View Items")
        print("4. Back to Main Menu")

        option = input("Enter your choice (1-4): ")

        if option == "1":
            name = input("Enter item name: ")
            quantity = input("Enter quantity: ")
            add_update_item(name, quantity)
        elif option == "2":
            name = input("Enter item name to remove: ")
            remove_item(name)
        elif option == "3":
            view_items()
        elif option == "4":
            break
        else:
            print("Invalid option, please try again.")

# Financial Management
def finance_management():
    global income, expenses
    while True:
        print("\nFinancial Management")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Profit")
        print("4. Back to Main Menu")

        option = input("Enter your choice (1-4): ")

        if option == "1":
            income += float(input("Enter income amount: "))
            save_data()  # Save the updated financial data
        elif option == "2":
            expenses += float(input("Enter expense amount: "))
            save_data()  # Save the updated financial data
        elif option == "3":
            print(f"Profit: {cal_profit()}")  # Calculate and display profit
        elif option == "4":
            break  # Return to main menu
        else:
            print("Invalid option, please try again.")

# Feedback Management
def feedback_management():
    while True:
        print("\nCustomer Feedback")
        print("1. Add Feedback")
        print("2. View Feedback")
        print("3. Back to Main Menu")

        option = input("Enter your choice (1-3): ")

        if option == "1":
            feedback = input("Enter customer feedback: ")
            add_feedback(feedback)  # Add the feedback to the list and save it
        elif option == "2":
            view_feedback()  # View all feedback
        elif option == "3":
            break  # Return to the main menu
        else:
            print("Invalid option, please try again.")

# Start the program
main_menu()
