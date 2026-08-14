def main():
    # Loop until user types in correct format
    while True:
        try:
            text = input("Fraction: ").strip()
            x, y = text.split("/")
            x = int(x)
            y = int(y)
            z = x / y
            if z > 1:
                continue
            elif z < 0:
                continue
            break
        except (ValueError, ZeroDivisionError):
            pass

    # Outcomes
    if z >= 0.99:
        print("F")
    elif z <= 0.01:
        print("E")
    else:
        print(f"{int(round(z, 2) * 100)}%")


main()