import sys
import random

moves = ["rock", "paper", "scissors", "Rock", "Paper", "Scissors"]

print()

if len(sys.argv) > 1:
    test_str = sys.argv[1]
else:
    test_str = "abcdefghijklmnopqrstuvwxyz"

if test_str not in moves:
    sys.exit(f"Incorrect move: {test_str}")

player_choice = moves.index(test_str) % 3
print(f"Player selects: {test_str} - {player_choice}")

house_choice = int(random.choice("012"))

print(f"House  selects: {moves[house_choice]} - {house_choice}")


