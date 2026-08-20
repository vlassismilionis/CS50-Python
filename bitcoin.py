import requests
import sys

def main():
    try:
        # Exiting if user doesn't enter at least 2 arguements
        if len(sys.argv) < 2:
            sys.exit("Missing command-line argument")

        # Getting amount of bitcoins 
        n = float(sys.argv[1])

        # Gettings the JSON fiel from CoinCap API and storing it in a variable
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=ec1ae68ce634fcab7c0f786d6fa94497773ba491092b3509cd30bf3cc9f5542f")
        o = response.json()

        # Locating the price inside the JSON file
        price = float(o["data"]["priceUsd"])

        result = n * price
        print(f"${result:,.4f}")
    except requests.RequestException:
        sys.exit()
    except ValueError: 
        sys.exit("Command-line argument is not a number")


main()