def main():
    #Getting input from user
    n = input("Input: ").strip()
    name = list(n)

    #Calling function to convert the text
    converter(name)

    #Calling function to print the text char by char
    printing(name)


def converter(text):
    for _ in range(len(text)):
        match text[_]:
            case "a":
                text[_] = ""
            case "A":
                text[_] = ""
            case "e":
                text[_] = ""
            case "E":
                text[_] = ""
            case "i":
                text[_] = ""
            case "I":
                text[_] = ""
            case "o":
                text[_] = ""
            case "O":
                text[_] = ""
            case "u":
                text[_] = ""
            case "U":
                text[_] = ""


def printing(text):
    for _ in range(len(text)):
        print(text[_], end="")
    print()


main()