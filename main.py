import random
rng = random.randint(1, 100)
guesses = 0
game_started = False
difficulty = input("Easy or Hard? ").lower()
if difficulty == "easy":
    guesses = 10
    game_started = True
elif difficulty == "hard":
    guesses = 5
    game_started = True
else:
    print("I didn't understand that.")
while game_started == True:
    player_guess = input(f"Guess the number!  You have {guesses} attempts left) ")