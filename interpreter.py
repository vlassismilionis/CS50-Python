def main():
    x, y, z = input("Expression: ").strip().split(" ")
    x = int(x)
    z = int(z)

    if y == "+":
        print(float(x + z))
    elif y == "-":
        print(float(x - z))
    elif y == "*":
        print(float(x * z))
    elif y == "/":
        print(float(x / z))
    else:
        print("y has to be an operator such as : +, -, *, /")

main()