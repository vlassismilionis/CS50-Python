import sys

def main():
    # Checking arguements
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguements")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguements")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        # Counter
        s = 0

        with open(sys.argv[1]) as file:
            for line in file:
                # If line is empty ignore
                if line.strip() == "":
                    continue
                # If line isn't a comment then count it 
                elif not line.lstrip().startswith("# "):
                    s += 1    
    # If file doesn't exist then exit
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(s)


main()