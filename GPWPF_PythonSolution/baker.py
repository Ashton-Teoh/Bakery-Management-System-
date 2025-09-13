# Constants for ingredient validation (could be expanded as needed)
INGREDIENTS_FILE = 'ingredients.txt'

# File names
RECIPES_FILE = 'recipes.txt'
PRODUCTION_FILE = 'production_records.txt'
EQUIPMENT_FILE = 'equipment_issues.txt'


def read_file(file_name):
    """Reads data from a file and returns it as a list of lines."""
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Error: '{file_name}' file not found.")
        return []


def write_file(file_name, data, mode='a'):
    """Writes data to a file."""
    with open(file_name, mode) as file:
        file.write(data + '\n')


# Recipe Management: create, update, or delete recipes
def manage_recipes():
    recipes = {}
    # Load existing recipes
    for line in read_file(RECIPES_FILE):
        name, ingredients = line.strip().split(':')
        recipes[name] = ingredients.split(',')

    while True:
        print("\n--- Recipe Management ---")
        print("1. Add Recipe")
        print("2. Update Recipe")
        print("3. Delete Recipe")
        print("4. View All Recipes")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma separated): ").split(',')
            recipes[name] = ingredients
            write_file(RECIPES_FILE, f"{name}:{','.join(ingredients)}")  # Write new recipe to file
            print(f"Recipe for {name} has been added successfully!")
        elif choice == '2':
            name = input("Enter the recipe name you wish to update: ")
            if name in recipes:
                ingredients = input("Enter new ingredients (comma separated): ").split(',')
                recipes[name] = ingredients
                # Update the file
                with open(RECIPES_FILE, 'w') as file:
                    for r_name, r_ingredients in recipes.items():
                        file.write(f"{r_name}:{','.join(r_ingredients)}\n")
                print(f"Recipe for {name} updated successfully!")
            else:
                print("Recipe not found!")
        elif choice == '3':
            name = input("Enter the recipe name you wish to delete: ")
            if name in recipes:
                del recipes[name]
                # Update the file
                with open(RECIPES_FILE, 'w') as file:
                    for r_name, r_ingredients in recipes.items():
                        file.write(f"{r_name}:{','.join(r_ingredients)}\n")
                print(f"Recipe for {name} has been deleted successfully!")
            else:
                print("Recipe not found!")
        elif choice == '4':
            print("\n--- All Recipes ---")
            for recipe, ingredients in recipes.items():
                print(f"{recipe}: {', '.join(ingredients)}")
        elif choice == '5':
            break
        else:
            print("Invalid option! Please try again.")


# Inventory Check: to verify the availability of ingredients
def read_ingredients_from_file(file_name):
    """Reads ingredients from a file and returns them as a list."""
    return read_file(file_name)  # Simplified

def write_ingredient_to_file(file_name, ingredient):
    """Writes a new ingredient to the file."""
    write_file(file_name, ingredient)

def inventory_check():
    """Checks the availability of ingredients and allows adding new ones."""
    ingredients = read_ingredients_from_file(INGREDIENTS_FILE)  # Load ingredients from file

    while True:
        print("\n--- Inventory Check ---")
        ingredient = input("Enter the ingredient you wish to check (or 'add' to add a new ingredient, 'back' to return): ").strip().lower()
        
        if ingredient == 'back':
            break
        elif ingredient == 'add':
            new_ingredient = input("Enter the ingredient to add: ").strip().lower()
            if new_ingredient in ingredients:
                print(f"{new_ingredient.capitalize()} is already in the inventory.")
            else:
                write_ingredient_to_file(INGREDIENTS_FILE, new_ingredient)  # Write new ingredient to the file
                ingredients.append(new_ingredient)  # Update the local list
                print(f"{new_ingredient.capitalize()} has been added to the inventory.")
        elif ingredient in ingredients:
            print(f"{ingredient.capitalize()} is available.")
        else:
            print(f"{ingredient.capitalize()} is not available.")


# Production Recording
def record_production():
    production_records = []
    # Load existing production records
    for line in read_file(PRODUCTION_FILE):
        records = line.strip().split(',')
        if len(records) == 4:  # Ensure there are exactly 4 elements
            production_records.append({
                'product_name': records[0],
                'quantity': float(records[1]),
                'batch_number': records[2],
                'expiration_date': records[3]
            })

    while True:
        print("\n--- Production Record ---")
        print("1. Add Production Record")
        print("2. View Production Records")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            product_name = input("Enter product name: ")
            quantity = input("Enter quantity produced: ")
            batch_number = input("Enter batch number: ")
            expiration_date = input("Enter expiration date (YYYY-MM-DD): ")

            try:
                quantity = float(quantity)  # Basic validation for quantity
                production_records.append({
                    'product_name': product_name,
                    'quantity': quantity,
                    'batch_number': batch_number,
                    'expiration_date': expiration_date
                })
                write_file(PRODUCTION_FILE, f"{product_name},{quantity},{batch_number},{expiration_date}")  # Write to file
                print(f"Record for {product_name} added successfully!")
            except ValueError:
                print("Invalid quantity! Please enter a valid number.")
        elif choice == '2':
            print("\n--- Production Records ---")
            for record in production_records:
                print(f"Product: {record['product_name']}, Quantity: {record['quantity']}, Batch: {record['batch_number']}, Expiration: {record['expiration_date']}")
        elif choice == '3':
            break
        else:
            print("Invalid option! Please try again.")


# Equipment Management
def manage_equipment():
    equipment_issues = []
    # Load existing equipment issues
    for line in read_file(EQUIPMENT_FILE):
        if ':' in line:  # Check for valid line
            equipment_name, issue = line.strip().split(':', 1)
            equipment_issues.append({'equipment_name': equipment_name, 'issue': issue})

    while True:
        print("\n--- Equipment Management ---")
        print("1. Report Malfunction or Maintenance")
        print("2. View Reported Issues")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            equipment_name = input("Enter equipment name: ")
            issue = input("Describe the issue: ")
            equipment_issues.append({'equipment_name': equipment_name, 'issue': issue})
            write_file(EQUIPMENT_FILE, f"{equipment_name}:{issue}")  # Write to file
            print(f"Issue for {equipment_name} reported successfully!")
        elif choice == '2':
            print("\n--- Equipment Issues ---")
            for issue in equipment_issues:
                print(f"Equipment: {issue['equipment_name']}, Issue: {issue['issue']}")
        elif choice == '3':
            break
        else:
            print("Invalid option! Please try again.")


# Main Program Menu
def mainbaker():
    while True:
        print("\n--- The Baker's ---")
        print("1. Recipe Management ")
        print("2. Inventory Check")
        print("3. Record Production")
        print("4. Equipment Management")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manage_recipes()
        elif choice == '2':
            inventory_check()
        elif choice == '3':
            record_production()
        elif choice == '4':
            manage_equipment()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    mainbaker()






    
