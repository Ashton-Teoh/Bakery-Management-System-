# Define constants
DISCOUNT_LIMIT = 100
RECIPE_FILE = "recipe.txt"  # Path to the product file


# Function to read products from the recipe.txt file
def load_products():
    products = []
    try:
        with open(RECIPE_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    products.append(line.split(","))  # Split each line into product details
        return products
    except FileNotFoundError:
        print(f"Error: '{RECIPE_FILE}' file not found.")
        return []


# Function to write products back to the recipe.txt file
def save_products(products):
    with open(RECIPE_FILE, "w") as file:
        for product in products:
            file.write(",".join(product) + "\n")


# 1. Product Display: Access a digital menu or product catalogue to view available items.
def display_products():
    products = load_products()
    if not products:
        print("No products available.")
        return
    print("\n--- Product Catalog ---")
    for idx, product in enumerate(products, 1):
        try:
            name, price, discount = product
            print(f"{idx}. Product: {name}, Price: RM {float(price):.2f}, Discount: {discount}%")
        except ValueError:
            print(f"Invalid format in product entry: {product}")
    print("------------------------")


# 2. Manage Discount: Add, modify, or delete discounts or promotions for items.
def manage_discount(name, action, discount=0):
    """
    Manages the discount for a product.

    :param name: Name of the product to manage
    :param action: 'add', 'modify', or 'delete' for managing discounts
    :param discount: Discount percentage to be added or modified
    """
    products = load_products()
    product_found = False  # Track if the product is found

    for product in products:
        if product[0].lower() == name.lower():  # Case insensitive match
            product_found = True
            if action == "add" or action == "modify":
                if 0 <= discount <= DISCOUNT_LIMIT:
                    product[2] = str(discount)
                    print(f"Discount for '{name}' updated to {discount}%.")
                    save_products(products)  # Save the updated product list
                    return
                else:
                    print("Invalid discount! Must be between 0 and 100%.")
                    return
            elif action == "delete":
                product[2] = "0"  # Reset discount to 0%
                print(f"Discount for '{name}' has been removed.")
                save_products(products)  # Save the updated product list
                return

    if not product_found:
        print(f"Product '{name}' not found.")


# 3. Transaction Completion: Generate receipts for customers.
def complete_transaction(cart):
    products = load_products()
    total_cost = 0
    print("\n--- Receipt ---")
    for item in cart:
        for product in products:
            name, price, discount = product
            if name.lower() == item.lower():
                final_price = calculate_discounted_price(float(price), float(discount))
                print(f"{name}: Original Price: RM {float(price):.2f}, Price after Discount: RM {final_price:.2f}")
                total_cost += final_price
                break
        else:
            print(f"Product '{item}' not found.")
    print(f"Total: RM {total_cost:.2f}")
    print("-----------------")


# 4. Reporting: Generate reports on sales performance and product popularity.
def generate_report(sales_report):
    if not sales_report:
        print("No transactions available.")
        return

    print("\n--- Sales Report ---")
    total_sales = 0
    product_sales = {}

    for item, final_price in sales_report:
        if item in product_sales:
            product_sales[item]["count"] += 1
            product_sales[item]["total_sales"] += final_price
        else:
            product_sales[item] = {"count": 1, "total_sales": final_price}

    for product, data in product_sales.items():
        print(f"Product: {product}, Sold: {data['count']} times, Total Sales: RM {data['total_sales']:.2f}")
        total_sales += data["total_sales"]

    print(f"Total Sales Revenue: RM {total_sales:.2f}")
    print("--------------------")


# Helper function to calculate the discounted price
def calculate_discounted_price(price, discount):
    return price * (1 - discount / 100)


def maincashier():
    sales_report = []  # This will track products sold and their final price after discount

    while True:
        print("\n1. Display Products")
        print("2. Manage Discount")
        print("3. Complete Transaction")
        print("4. Generate Sales Report")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            display_products()

        elif choice == '2':
            name = input("Enter product name to apply or delete discount: ").strip()
            action = input(
                "Do you want to add/modify or delete the discount? (Enter 'add', 'modify', or 'delete'): ").strip().lower()

            if action in ['add', 'modify']:
                try:
                    discount = float(input("Enter discount percentage (0-100): ").strip())
                    manage_discount(name, action, discount)
                except ValueError:
                    print("Invalid discount input! Please enter a valid number between 0 and 100.")
            elif action == 'delete':
                manage_discount(name, action)
            else:
                print("Invalid action! Please enter 'add', 'modify', or 'delete'.")

        elif choice == '3':
            cart = input("Enter products bought (comma-separated): ").strip().split(',')
            cart = [item.strip() for item in cart]  # Clean up the input
            complete_transaction(cart)

            # Add to sales report after completing transaction
            for item in cart:
                for product in load_products():
                    name, price, discount = product
                    if name.lower() == item.lower():
                        final_price = calculate_discounted_price(float(price), float(discount))
                        sales_report.append((name, final_price))

        elif choice == '4':
            generate_report(sales_report)

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    maincashier()