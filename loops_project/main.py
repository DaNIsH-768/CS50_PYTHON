import random as rd

GUESSED = []
NUMBER = rd.randint(1, 100)
guesses = 0

while True:
    try:
        guess = int(input("Guess: "))
    except:
        print("Invalid number")
        continue

    if guess in GUESSED:
        print("Already guessed.")
        print("guesses:", GUESSED)
        continue

    GUESSED.append(guess)
    guesses += 1

    if guess == NUMBER:
        print(f"You did it. You guessed it in {guesses} guesses.")
        break
    else:
        if guess < NUMBER:
            print("Too Low.")
        else:
            print("Too High")


    
