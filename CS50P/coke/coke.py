def valid_coin(coin):
    # Constants for accepted coin denominations
    ACCEPTED_COINS = [25, 10, 5]

    return coin in ACCEPTED_COINS

def insert_coins():
    # Constants
    PRICE = 50

    # Variables
    total_inserted = 0

    # Coin insertion process
    while total_inserted < PRICE:
        coin = int(input("Insert a coin: "))
        if valid_coin(coin):
            total_inserted += coin
        if total_inserted < PRICE:
            print(f"Amount Due: {PRICE - total_inserted}")

    # Calculating and outputting change
    return total_inserted - PRICE

def main():
    change = insert_coins()
    print(f"Change Owed: {change}")

# Call main function
if __name__ == "__main__":
    main()
