def main():
    plate = input("Plate: ").strip().upper()

    # Calling function to validate the plate
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ss = list(s)

    # Calling functions for the requirements
    if starting_letters(ss) and m_char(ss) and numbers(ss) and punct(ss):
        return True
    else:
        return False


def starting_letters(text):
    # Counter
    i = 0

    # If there is only 1 char return False
    if len(text) == 1:
        return False

    # Checking if first 2 chars are letters with a counter
    for _ in range(2):
        if text[_].isalpha():
            i += 1
        else: 
            continue

    if i > 1:
        return True
    else:
        return False


def m_char(text):
    # Checking if plate contains max 6 & min 2 characters
    if 2 <= len(text) <= 6:
        return True
    else:
        return False 


def numbers(text):
    # Counter for letters
    i = 0
    # Counter for numbers
    k = 0

    # Counting how many letters and numbers the input has
    for _ in range(len(text)):
        if text[_].isalpha():
            i += 1
        else:
            k += 1
            continue

    # Locating the first number
    for _ in range(len(text)):
        if text[_].isalpha():
            continue
        else:
            j = text[_] # First Number's Value
            j1 = _ # First Number's Index
            # Return False if first number is 0
            if j == "0":
                return False
            break

    # Locating the last number (If there is more than 1 number)
    if k > 1:
        for _ in range(len(text)):
            if text[_].isalpha():
                continue
            else:
                z = _ # Last Number's Index

    # If there are no numbers return True
    if i == len(text):
        return True 
    else:
        # If there is only 1 number and the last char is letter, return False 
        if k == 1 and text[len(text) - 1].isalpha():
            return False
        # If there is more than 1 number and the last char is letter, return False
        elif k > 1 and text[len(text) - 1].isalpha():
            return False
        # If there is more than 1 number and between them there is atleast 1 letter, return False
        else:
            for _ in range(j1, z):
                if text[_].isalpha():
                    return False
                else:
                    continue
            return True
            
                  
def punct(text):
    # Checking for punctuation marks
    for _ in range(len(text)):
        match text[_]:
            case ".":
                return False
            case " ":
                return False
            case "?":
                return False
            case "!":
                return False
    return True


main()