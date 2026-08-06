def main():
    text = input()
    print(convert(text))

def convert(str):
    str = str.replace(":)", "🙂").replace(":(", "🙁")
    return str

main()
