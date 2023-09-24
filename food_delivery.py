class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

    def place_order(self, food_items):
        self.orders.append(food_items)

    def get_order_history(self):
        return self.orders

food_items = [
    FoodItem("Tandoori Chicken (4 pieces)", "4 pieces", 240, 0, 10),
    FoodItem("Vegan Burger (1 Piece)", "1 piece", 320, 0, 15),
    FoodItem("Truffle Cake (500gm)", "500gm", 900, 0, 5),
]

users = [
    User("Edyoda", "3856331445", "edyoda@edyoda.com", "123 Main St", "password123"),
    User("bhavani", "2422242142", "bhavani@edyoda.com", "456 Oak Ave", "securepass"),
]

def main():
    print("Welcome to Food Ordering App!")
    while True:
        print("\nOptions:")
        print("1. User Login")
        print("2. Admin Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            logged_in_user = user_login()
            if logged_in_user:
                user_menu(logged_in_user)
        elif choice == "2":
            admin_menu()
        elif choice == "3":
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def user_login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    user = next((user for user in users if user.email == email and user.password == password), None)
    if user:
        return user
    else:
        print("Invalid email or password.")
        return None

def user_menu(user):
    while True:
        print("\nUser Menu:")
        print("1. Place New Order")
        print("2. Order History")
        print("3. Update Profile")
        print("4. Logout")
        user_choice = input("Select an option: ")

        if user_choice == "1":
            place_order(user)
        elif user_choice == "2":
            view_order_history(user)
        elif user_choice == "3":
            update_profile(user)
        elif user_choice == "4":
            print("Logging out.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def place_order(user):
    print("Available Food Items:")
    for index, food_item in enumerate(food_items, start=1):
        print(f"{index}. {food_item.name} [{food_item.quantity}] [INR {food_item.price}]")

    selected_indices = input("Enter the indices of the items you want to order (comma-separated): ")
    selected_indices = [int(index) - 1 for index in selected_indices.split(",")]

    selected_items = [food_items[index] for index in selected_indices]
    user.place_order(selected_items)

    print("Order placed successfully.")

def view_order_history(user):
    print("Order History:")
    for index, order in enumerate(user.get_order_history(), start=1):
        print(f"Order {index}:")
        for food_item in order:
            print(f"- {food_item.name} [{food_item.quantity}] [INR {food_item.price}]")
        print()

def update_profile(user):
    print("Update Profile:")
    user.full_name = input("Enter your full name: ")
    user.phone_number = input("Enter your phone number: ")
    user.address = input("Enter your address: ")
    user.password = input("Choose a new password: ")

    print("Profile updated successfully.")

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add New Food Item")
        print("2. Edit Food Item")
        print("3. View Food Items")
        print("4. Remove Food Item")
        print("5. Back to Main Menu")
        admin_choice = input("Select an option: ")

        if admin_choice == "1":
            add_food_item()
        elif admin_choice == "2":
            edit_food_item()
        elif admin_choice == "3":
            view_food_items()
        elif admin_choice == "4":
            remove_food_item()
        elif admin_choice == "5":
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def add_food_item():
    name = input("Enter the name of the food item: ")
    quantity = input("Enter the quantity of the food item: ")
    price = float(input("Enter the price of the food item: "))
    discount = float(input("Enter the discount percentage: "))
    stock = int(input("Enter the stock amount: "))

    new_food_item = FoodItem(name, quantity, price, discount, stock)
    food_items.append(new_food_item)
    print("Food item added .")

def edit_food_item():
    view_food_items()
    food_id = int(input("Enter the FoodID of the item you want to edit: "))
    food_item = next((item for item in food_items if item.food_id == food_id), None)

    if food_item:
        food_item.name = input("Enter the new name: ")
        food_item.quantity = input("Enter the new quantity: ")
        food_item.price = float(input("Enter the new price: "))
        food_item.discount = float(input("Enter the new discount percentage: "))
        food_item.stock = int(input("Enter the new stock amount: "))
        print("Food item edited successfully.")
    else:
        print("Food item not found.")

def view_food_items():
    print("Food Items:")
    for food_item in food_items:
        print(f"FoodID: {food_item.food_id}")
        print(f"Name: {food_item.name}")
        print(f"Quantity: {food_item.quantity}")
        print(f"Price: INR {food_item.price}")
        print(f"Discount: {food_item.discount}%")
        print(f"Stock: {food_item.stock}")
        print()

def remove_food_item():
    view_food_items()
    food_id = int(input("Enter the FoodID of the item you want to remove: "))
    food_item = next((item for item in food_items if item.food_id == food_id), None)

    if food_item:
        food_items.remove(food_item)
        print("Food item removed successfully.")
    else:
        print("Food item not found.")

if __name__ == "__main__":
    main()