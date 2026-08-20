import random

def main():
    # Calling the function to get level from user
    level = get_level()

    # score-counter
    w = 0

    # Loop for all 10 math problems
    for _ in range(10):
        # mistake-counter
        s = 0
        # Calling the function to generate random numbers regarding the level user entered
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        while True:
            try:
                # Getting answer from user
                answer = int(input(f"{x} + {y} = "))
                # If answer is correct then proceed to next problem and reset mistake-counter
                if answer == z:
                    s = 0
                    w += 1
                    break
                # If answer not correct then print following message, increment mistake-counter by 1 and reprompt user for answer
                else:
                    print("EEE")
                    s += 1
                    # If mistake-counter reaches 3 then print the answer, reset mistake-counter and proceed to next problem
                    if s == 3:
                        print(f"{x} + {y} = {z}")
                        s = 0
                        break
                    continue
            except ValueError:
                pass

    print(f"Score: {w}")
    

def get_level():
    while True:
        try:
            # Getting level from user
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
            else:
                continue
        except ValueError:
            pass


def generate_integer(level):
    # Generating ints based on the level the user entered
    match level:
        case 1:
            return random.randint(0,9)
        case 2:
            return random.randint(10,99)
        case 3:
            return random.randint(100,999)


if __name__ == "__main__":
    main()