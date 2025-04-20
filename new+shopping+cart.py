#Shopping Cart Program with Quantity Tracking and Formatted Display

def display_menu():
    print("\nWelcome to the Shopping Cart Program!")
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

def add_item(cart, prices, quantities):
    item = input("What item would you like to add? ").strip()
    while True:
        try:
            price = float(input(f"What is the price of '{item}'? ").strip())
            if price < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid price. Please enter a valid number.")
    while True:
        try:
            quantity = int(input(f"How many '{item}' would you like to add? ").strip())
            if quantity < 1:
                raise ValueError
            break
        except ValueError:
            print("Invalid quantity. Please enter a whole number greater than 0.")
    
    cart.append(item)
    prices.append(price)
    quantities.append(quantity)
    print(f"{quantity} '{item}' added to the cart.")

def view_cart(cart, prices, quantities):
    if not cart:
        print("Your shopping cart is empty.")
    else:
        print("\nThe contents of the shopping cart are:")
        for i, (item, price, quantity) in enumerate(zip(cart, prices, quantities), start=1):
            print(f"{i}. {item} - ${price:.2f} x {quantity} = ${price * quantity:.2f}")

def remove_item(cart, prices, quantities):
    if not cart:
        print("Your cart is empty. Nothing to remove.")
        return
    view_cart(cart, prices, quantities)
    while True:
        try:
            index = int(input("Which item number would you like to remove? ").strip()) - 1
            if 0 <= index < len(cart):
                removed_item = cart.pop(index)
                removed_price = prices.pop(index)
                removed_quantity = quantities.pop(index)
                print(f"Removed {removed_quantity} '{removed_item}' from the cart.")
                break
            else:
                print("Invalid item number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def compute_total(prices, quantities):
    total = sum(price * quantity for price, quantity in zip(prices, quantities))
    print(f"The total price of the items in the shopping cart is ${total:.2f}")

def main():
    cart = []
    prices = []
    quantities = []
    
    while True:
        display_menu()
        choice = input("Please enter an action: ").strip()
        if choice == "1":
            add_item(cart, prices, quantities)
        elif choice == "2":
            view_cart(cart, prices, quantities)
        elif choice == "3":
            remove_item(cart, prices, quantities)
        elif choice == "4":
            compute_total(prices, quantities)
        elif choice == "5":
            print("Thank you. Goodbye.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
