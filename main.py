import random
import sys
def game_loop():
    rng = random.randint(1, 100)
    guesses = 0
    game_started = False
    while game_started == False:
        difficulty = input("""Easy, Medium, or Hard?
        Easy: 10 guesses, and the number can only be between 1 and 50
        Medium: 10 guesses, and the number will be between 1 and 100
        Hard: 5 guesses.
        What shall it be? """).lower()
        if difficulty == "easy":
            guesses = 10
            game_started = True
            rng = random.randint(1, 50)
        elif difficulty == "medium":
            guesses = 10
            game_started = True
        elif difficulty == "hard":
            guesses = 5
            game_started = True
        elif difficulty == "spam":
            guesses == 100
            game_started = True
        else:
            print("I didn't understand that.")
    while game_started == True:
        if guesses == 0:
            break
        if guesses == 0:
            game_started = False
        player_guess = int(input(f"Guess the number!  You have {guesses} attempts left) "))
        if player_guess > rng:
            guesses -= 1
            print(f"Too high! ({guesses} attempts left)")
        elif player_guess < rng:
            guesses -= 1
            print(f"Too low! ({guesses} attempts left)")
        elif player_guess == rng:
            print("Correct!")
            break
    continue_playing = input("Continue? ").lower()
    if continue_playing == "yes":
        game_loop()
    else:
        sys.exit()