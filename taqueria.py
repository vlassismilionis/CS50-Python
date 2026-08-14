def main():
    # The Menu 
    dictionary = {
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

    # Variable used to sum every cost
    s = 0.00

    # Loop to get as many items as user wants until user presses Ctrl + D
    while True:
        try:
            item = input("Item: ").strip().title()
            s = dictionary[item] + s
            print(f"Total: ${s:.2f}")
        except KeyError:
            pass
        except EOFError:
            break

    print()


main()