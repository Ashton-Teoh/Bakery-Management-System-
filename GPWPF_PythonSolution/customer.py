# Bakery Management System

# Constants
CUSTOMER_FILE = 'customers.txt'
PRODUCT_FILE = 'products.txt'
CART_FILE = 'cart.txt'
ORDER_FILE = 'orderscustomer.txt'
REVIEW_FILE = 'review.txt'


# Helper function to read data from a file
def read_file(file_name):
    """Reads data from a file and returns it as a list of lines."""
    try:
        with open(file_name, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []


# Helper function to write data to a file
def write_file(file_name, data, mode='a'):
    """Writes data to a file."""
    with open(file_name, mode) as file:
        file.write(data + '\n')


# Customer Management Functions
def create_account():
    """Registers a new customer."""
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    address = input("Enter your address: ")

    write_file(CUSTOMER_FILE, f"{email},{password},{name},{address}")
    print("Account created successfully!")


def login():
    """Customer login."""
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    customers = read_file(CUSTOMER_FILE)
    for customer in customers:
        details = customer.strip().split(',')
        if details[0] == email and details[1] == password:
            print(f"Welcome, {details[2]}!")
            return True
    print("Login failed. Please try again.")
    return False


# Product Browsing
def products_browsing():
    """Browsing all available products."""
    products = read_file(PRODUCT_FILE)  # Read products from the file
    if not products:
        print("No products available.")
        return
    
    print("\n--- Product Catalog ---")
    for product in products:
        details = product.strip().split(',')
        product_id, name, price = details
        print(f"Products ID: {product_id}, Product: {name}, Price: RM{price}")
    print("------------------------")


# Cart Management Functions
def add_to_cart():
    """Adds a product to the customer's cart."""
    product_id = input("Enter the product ID to add to cart: ")
    quantity = input("Enter quantity: ")

    write_file(CART_FILE, f"{product_id},{quantity}")
    print("Product added to cart!")


def view_cart():
    """Displays cart."""
    cart = read_file(CART_FILE)
    if cart:
        print("Your Cart:")
        for item in cart:
            details = item.strip().split(',')
            if len(details) == 2:  # Ensure there are exactly 2 elements: product ID and quantity
                print(f"Product ID: {details[0]}, Quantity: {details[1]}")
            else:
                print("Error: Incorrect cart item format.")
    else:
        print("Your cart is empty.")



def remove_from_cart():
    """Removes a product from the cart."""
    product_id = input("Enter the product ID to remove: ")
    cart = read_file(CART_FILE)
    updated_cart = [item for item in cart if not item.startswith(product_id)]

    with open(CART_FILE, 'w') as file:
        for item in updated_cart:
            file.write(item)
    print("Product have been removed from cart.")


# Order Management Functions
def place_order():
    """Places an order."""
    cart = read_file(CART_FILE)
    if cart:
        write_file(ORDER_FILE, f"Order: {cart}", 'a')
        print("Order placed successfully!")
    else:
        print("Your cart is empty.")


def track_order():
    """Displays the status of the current order."""
    orders = read_file(ORDER_FILE)
    if orders:
        print("Your Orders:")
        for order in orders:
            print(order.strip())
    else:
        print("You have no current orders.")


def cancel_order():
    """Cancels the most recent order."""
    orders = read_file(ORDER_FILE)
    if orders:
        # Remove the last order
        with open(ORDER_FILE, 'w') as file:
            file.writelines(orders[:-1])
        print("Most recent order has been canceled.")
    else:
        print("No orders to cancel.")


# Review Management Functions
def manage_reviews():
    """Handles adding and displaying product reviews."""
    while True:
        print("\nReview Management Menu")
        print("1. Add Review")
        print("2. Display Reviews")
        print("3. Back to Main Menu")

        review_choice = input("Enter your choice (1-3): ")

        if review_choice == '1':
            product_id = input("Enter the product ID to review: ")
            review = input("Enter your review: ")
            write_file(REVIEW_FILE, f"{product_id},{review}")
            print("Review submitted!")
        elif review_choice == '2':
            product_id = input("Enter the product ID to see reviews: ")
            reviews = read_file(REVIEW_FILE)

            print(f"Reviews for Product ID: {product_id}")
            found = False
            for review in reviews:
                details = review.strip().split(',')
                if details[0] == product_id:
                    print(f"Review: {details[1]}")
                    found = True
            if not found:
                print("No reviews found for this product.")
        elif review_choice == '3':
            break  # Go back to the main menu
        else:
            print("Invalid choice, please try again.")


# Main Program Flow
def maincustomer():
    """Main function to navigate the bakery management system."""

    # Combined account creation and login process
    while True:
        print("\nWelcome to the Bakery Management System")
        print("1. Login (If you already have an account)")
        print("2. Create Account (If you don't have an account)")
        initial_choice = input("Enter your choice (1 for Login, 2 for Create Account): ")

        if initial_choice == '1':
            if login():
                break  # Proceed only if login is successful
        elif initial_choice == '2':
            create_account()
            if login():  # Immediately prompt login after account creation
                break
        else:
            print("Invalid choice, please try again.")

    # After successful login, display the main menu
    while True:
        print("\nMain Menu")
        print("1. Products Browsing")
        print("2. Cart Management")  # Combined option for cart management
        print("3. Order Management")  # Combined option for order management
        print("4. Review Management")  # Combined option for review management
        print("5. Exit")

        choice = input("Enter your choice(1-5): ")

        if choice == '1':
            products_browsing()
        elif choice == '2':
            while True:
                print("\nCart Management Menu")
                print("1. Add to Cart")
                print("2. View Cart")
                print("3. Remove from Cart")
                print("4. Back to Main Menu")

                cart_choice = input("Enter your choice (1-4): ")

                if cart_choice == '1':
                    add_to_cart()
                elif cart_choice == '2':
                    view_cart()
                elif cart_choice == '3':
                    remove_from_cart()
                elif cart_choice == '4':
                    break  # Go back to the main menu
                else:
                    print("Invalid choice, please try again.")
        elif choice == '3':
            while True:
                print("\nOrder Management Menu")
                print("1. Place Order")
                print("2. Track Order")
                print("3. Cancel Order")  # Added cancel order option
                print("4. Back to Main Menu")

                order_choice = input("Enter your choice (1-4): ")

                if order_choice == '1':
                    place_order()
                elif order_choice == '2':
                    track_order()
                elif order_choice == '3':
                    cancel_order()  # Call cancel order function
                elif order_choice == '4':
                    break  # Go back to the main menu
                else:
                    print("Invalid choice, please try again.")
        elif choice == '4':
            manage_reviews()  # Calls the review management function
        elif choice == '5':
            print("Thank You!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    maincustomer()