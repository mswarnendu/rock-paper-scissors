import random

possibleChoices = ("rock", "paper", "scissors")

start = input(
    "Welcome to Rock Paper Scissors! Press Enter to continue.\n")
keepPlaying = "y"
wins = 0
attempts = 0
ties = 0
losses = 0

print("Rules:\n1. Do not put in any invalid inputs, these do count as attempts and can decrease your win rate.\n2. Have fun!\n")
tos = input("Press Enter after you have understood the rules.\n")

while keepPlaying == "y":
    playHuman = input(
        "State your move by typing in 'rock', 'paper', or 'scissors': ")
    playComp = random.choice(possibleChoices)
    print(f"The computer chooses {playComp}.")
    if playHuman.lower() == "rock":
        if playComp == "scissors":
            keepPlaying = input("You win! Continue playing? (y/n) ")
            print()
            wins += 1
        elif playComp == "paper":
            keepPlaying = input("You loose! Continue playing? (y/n) ")
            print()
            losses += 1
        else:
            keepPlaying = input("Tie! Continue playing? (y/n) ")
            print()
            ties += 1
    elif playHuman.lower() == "paper":
        if playComp == "scissors":
            keepPlaying = input("You loose! Continue playing? (y/n) ")
            print()
            losses += 1
        elif playComp == "paper":
            keepPlaying = input("Tie! Continue playing? (y/n) ")
            print()
            ties += 1
        else:
            keepPlaying = input("You win! Continue playing? (y/n) ")
            print()
            wins += 1
    elif playHuman.lower() == "scissors":
        if playComp == "rock":
            keepPlaying = input("You loose! Continue playing? (y/n) ")
            print()
            losses += 1
        elif playComp == "paper":
            keepPlaying = input("You win! Continue playing? (y/n) ")
            print()
            wins += 1
        else:
            keepPlaying = input("Tie! Continue playing? (y/n) ")
            print()
            ties += 1
    else:
        keepPlaying = input("Invalid move. Continue playing? (y/n) ")
        print()
    attempts += 1

winRate = (float)(wins)/attempts * 100

print(f"Win rate: {winRate}%")
print(f"Wins: {wins}")
print(f"Ties: {ties}")
print(f"Losses: {losses}")
print(f"Attempts: {attempts}")
