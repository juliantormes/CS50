import sys
import requests

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        sys.exit("Usage: python script.py <number_of_bitcoins>")

    # Attempt to convert the argument to a float
    try:
        number_of_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: The number of Bitcoins must be a numeric value.")

    # Query the CoinDesk API
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        bitcoin_price = data["bpi"]["USD"]["rate_float"]

        # Calculate the total cost
        total_cost = number_of_bitcoins * bitcoin_price
        print(f"${total_cost:,.4f}")

    except requests.RequestException:
        sys.exit("Error: Unable to retrieve data from CoinDesk API.")

if __name__ == "__main__":
    main()
