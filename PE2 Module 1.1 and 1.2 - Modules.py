import random
number = random.randint(1,101)
def main():
    guess = None
    
    while guess != number:
        try:
            guess = int(input("Guess a whole number between 1-100:"))
            if abs(guess - number) < 5:
                print("Very Hot")
            elif abs(guess - number) < 15:
                print("Hot")
            elif abs(guess - number) < 25:
                print("Cool")
            else:
                print("Very Cold")
    
        except ValueError:
            print("That's not a valid number. Please enter a number between 1-100")

    print("Congrats, you guessed the number!")

main()

