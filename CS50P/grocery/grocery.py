def make_list():
    # Initialize an empty dictionary to store grocery items
    grocery_items = {}
    while True:
        try:
            # Prompt the user for an item and convert it to lowercase
            item = input().strip().lower()
            if item:
                # Increment the count for the item in the dictionary
                grocery_items[item] = grocery_items.get(item, 0) + 1
        except EOFError:
            # Break the loop when user signals end of input (Ctrl+D)
            break
    # Return the dictionary of grocery items
    return grocery_items

def output_list(lst):
    # Iterate through the sorted items and print them in uppercase
    for item, count in sorted(lst.items()):
        print(f"{count} {item.upper()}")

def main():
    # Create the grocery list
    grocery_list = make_list()
    # Output the formatted grocery list
    output_list(grocery_list)

if __name__ == "__main__":
    main()
