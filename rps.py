import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    VALID_MOVES = 3

# valid moves array, including capitalized value,
# normalized using MOD division.
moves = ["rock", "paper", "scissors", "Rock", "Paper", "Scissors"]

print("*********************************")

if len(sys.argv) > 1:
    # Player command line argument.
    player_input = sys.argv[1]

    if len(sys.argv) == 3:
        # House command line argument, for testing.
        house_input = sys.argv[2]

        # Check for valid input.
        if house_input not in moves:
            sys.exit(f"Incorrect move: {house_input}")

        # Choice is an integer index into the moves array.
        house_choice = moves.index(house_input) % RPS.VALID_MOVES.value
    else:
        # Random house input if none given.
        house_choice = int(random.choice("012"))
        house_input = moves[house_choice]

else:
    # Default player input.
    player_input = "rock"

    # Random house input if none given.
    house_choice = int(random.choice("012"))
    house_input = moves[house_choice]

# Check for valid input.
if player_input not in moves:
    sys.exit(f"Incorrect move: {player_input}")

# Choice is an integer index into the moves array.
player_choice = moves.index(player_input) % RPS.VALID_MOVES.value

# Print the player/house choices and for now, the normalized int value.
print(f"Player selects: {player_input} - {player_choice}")
print(f"House  selects: {house_input} - {house_choice}\n")

# Determine winner, fall through to house wins if other conditions fail.
if ((player_choice == RPS.ROCK .value and house_choice == RPS.SCISSORS.value) or
    (player_choice == RPS.PAPER.value and house_choice == RPS.ROCK.value) or
    (player_choice == RPS.SCISSORS.value and house_choice == RPS.PAPER.value)):
   print("Player wins".center(30, "="))
elif player_choice == house_choice:
    print("Tie game".center(30, "="))
else:
    print("House wins".center(30, "="))
    
print()
