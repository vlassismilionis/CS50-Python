def main():
    #Getting input from user and turning string into a list of chars
    n = input("camelCase: ")
    name = list(n)

    #Counter
    i = 0

    #Finding the position of every uppercase letter (Max 2)
    for _ in range(len(name)):
        if name[_].isupper():
            if i > 0:
                y = _
                name[y] = "_" + name[y].lower()
                break
            x = _
            name[x] = "_" + name[x].lower()
            i += 1
        else:
            continue

    for _ in range(len(name)):
        print(name[_], end="")
    print()


main()