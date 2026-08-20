import random
import sys

def main():
    # Reprompting user until a positive int is entered
    while True:
        try:
            n = int(input("Level: ").strip())
            if n <= 0:
                continue
            else: 
                break
        except ValueError:
            pass

    # Getting a random positive int ranged between [1, n]
    number = random.randint(1, n)

    # Reprompting user for a guess until positive int is entered
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
            # Outputting result of guess
            else:
                if guess == number:
                    sys.exit("Just right!")
                elif guess > number:
                    print("Too large!")
                    continue
                else:
                    print("Too small!")
                    continue
        except ValueError:
            pass
    

main()