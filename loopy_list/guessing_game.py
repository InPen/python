# Author: Maria Peniche

# Set a variable, answer to "5"
answer = "5"
# Prompt the user for a guess and save it in a new variable, guess.
guess = input("guess a number to enter:")
print("you chose", guess)
# Create a while loop, ending when guess is equal to answer.
while True:
    if guess == answer:
        print("You guessed right, you may enter The Chamber of Secretsss")
    elif guess != answer:
        print("wrong numbersss, guessss again")
    else:
        print(guess)
# In the while loop, prompt the user for a new guess.
# After the while loop
