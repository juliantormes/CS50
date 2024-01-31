def main():
    menu = {
        "Baja Taco": 4.00,
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
    total = 0
    while True:
        item = input("Item: ").title()
        if item in menu:
            total += menu.get(item)
        if len(item) == 0:
            break
    print(f"Total: ${total:.2f}")
    
main()