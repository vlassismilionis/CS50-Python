import pyfiglet
import sys
import random

fonts = ["slant", "rectangles", "alphabet"]

def main():
    # Checking total number of arguements
    if len(sys.argv) == 1:
        # Printing text with a random choice of font
        text = input("Input: ")
        print(pyfiglet.figlet_format(text, font = random.choice(fonts)))
    else:
        try:
            if sys.argv[1] == "-f" or sys.argv[1] == "--font":
                # If user entered an invalid font, system exits
                if sys.argv[2] not in fonts:
                    sys.exit("invalid usage")
                text = input("Input: ")
                print(pyfiglet.figlet_format(text, font = sys.argv[2]))
            # If user entered an invalid arguement in the 2nd position, system exits
            else:
                sys.exit("Invalid usage")
        # If user did not enter a 3rd arguement, system exits
        except IndexError:
            sys.exit("Invalid usage")


main()