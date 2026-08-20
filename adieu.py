import sys

def main():
    # List of names
    names = []

    # Names counter
    s = 0

    # Reprompting user until a name gets entered and placed inside .names
    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)
            s += 1
        except EOFError:
            print()
            break
    
    # System exits if there is no name entered
    for _ in range(s - 1):
        if names[_] == " " or names[_] == "":
            sys.exit()

    # Printing the message regarding the amount of names given (s)
    if 1 < s < 3:
        print("Adieu, adieu, to ", end="")
        for name in names[:s - 2]:
            print(f"{name}", end=", ")
        print(f"{names[s - 2]}", end=" and ")
        print(f"{names[s - 1]}")
    elif s >= 3:
        print("Adieu, adieu, to ", end="")
        for name in names[:s - 2]:
            print(f"{name}", end=", ")
        print(f"{names[s - 2]}", end=", and ")
        print(f"{names[s - 1]}")
    else:
        print(f"Adieu, adieu, to {names[0]}")


main()