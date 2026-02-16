import random

secret = random.randint(1, 50)
guesses = []   # data structure (list)

print("Guess a number between 1 and 50")

while True:
    guess = int(input("Enter your guess: "))
    guesses.append(guess)

    if guess == secret:
        print("🎉 Correct Guess!")
        break
    elif guess < secret:
        print("Too Low")
    else:
        print("Too High")

print("Total guesses:", len(guesses))
print("Your guesses were:", guesses)
