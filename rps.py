import sys
import random

moves = ["rock", "paper", "scissors", "Rock", "Paper", "Scissors"]

print()

if len(sys.argv) > 1:
    player_input = sys.argv[1]
    if len(sys.argv) == 3:
        house_input = sys.argv[2]
        house_choice = moves.index(house_input) % 3
    else:
        house_choice = int(random.choice("012"))
        house_input = moves[house_choice]

else:
    player_input = "abcdefghijklmnopqrstuvwxyz"

if player_input not in moves:
    sys.exit(f"Incorrect move: {player_input}")

if house_input not in moves:
    sys.exit(f"Incorrect move: {house_input}")

player_choice = moves.index(player_input) % 3
print(f"Player selects: {player_input} - {player_choice}")

print(f"House  selects: {moves[house_choice]} - {house_choice}")

if (player_choice == 0 and house_choice == 2) or \
   (player_choice == 1 and house_choice == 0) or \
   (player_choice == 2 and house_choice == 1):
   print("player wins")
elif player_choice == house_choice:
    print("tie game")
else:
    print("house wins")
    
