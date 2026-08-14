def main():
    dict = {}

    # Loop to get as many items as user wants until user presses Ctrl + D
    while True:
        try:
            item = input("").strip().upper()
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1

        except KeyError:
            pass
        except EOFError:
            break

    sdict = sorted(dict)

    for item in sdict:
        print(f"{dict[item]} {item}")    


main()