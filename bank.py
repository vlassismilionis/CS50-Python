def main():
    x = input("Greeting: ").strip().lower()

    if startwhello(x):
        print("$0")
    elif startwh(x):
        print("$20")
    else:
        print("$100")

def startwhello(text):
    return text.startswith("hello")

def startwh(text):
    return text.startswith("h")

main()