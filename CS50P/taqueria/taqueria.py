def process_order(menu):
    """
    Process the user's order and calculate the total cost.

    Args:
    menu (dict): A dictionary containing items and their prices.

    Returns:
    float: The total cost of the order.
    """
    total = 0
    while True:
        try:
            item = input("Item: ").title()
            if item in menu:
                total += menu.get(item)
            print(f"Total: ${total:.2f}")
        except EOFError:
            break
    return total

def main():
    # Creating a menu with items and their prices
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    print("Choose one or more items from the menu.")
    print("Press enter when done.\n")

    # Process the order and calculate the total
    total = process_order(menu)
    print(f"Total order cost: ${total:.2f}")

if __name__ == "__main__":
    main()
