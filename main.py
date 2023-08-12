from random import randint
import os
from art import logo, player1, player2, tie

choices = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

def display_boar(choices):
    board = (f"| {choices[1]} | {choices[2]} | {choices[3]} |\n"
             f"| {choices[4]} | {choices[5]} | {choices[6]} |\n"
             f"| {choices[7]} | {choices[8]} | {choices[9]} |")
    print(board)

def check_turn(turn):
    if turn % 2 == 0:
        return '0'
    return 'X'


def check_for_win(choices):
# Horizontal winners
    if (choices[1] == choices[2] == choices[3]) or \
            (choices[4] == choices[5] == choices[6]) or \
            (choices[7] == choices[8] == choices[9]):
        return True
# Vertical winners
    elif (choices[1] == choices[4] == choices[7]) or \
            (choices[2] == choices[5] == choices[8]) or \
            (choices[3] == choices[6] == choices[9]):
        return True
# Diagonal winners
    elif (choices[1] == choices[5] == choices[9]) or \
            (choices[3] == choices[5] == choices[7]):
        return True

    return False

print(logo)
print("Let's see who starts!")
player_A = (input("Please enter first player name: ")).title()
player_B = input("Please enter second player name: ").title()
random_player = randint(1, 2)
if random_player == 1:
    player_1 = player_A
    player_2 = player_B
    print(f"{player_A} starts as 'X'!")
else:
    player_1 = player_B
    player_2 = player_A
    print(f"{player_B} starts as 'X'")

game_on = True
complete = False
turn = 0
prev_turn = -1

while game_on:
    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

    display_boar(choices)
    # When invalid input let the player know
    if prev_turn == turn:
        print("That's not a valid input. Try again!")
    prev_turn = turn
    if turn % 2 == 0:
        print(f"{player_1}'s turn:  Pick your spot or press 'q' to quit")
    else:
        print(f"{player_2}'s turn:  Pick your spot or press 'q' to quit")

    # print(f"Player " + str((turn % 2) + 1) + "'s turn: Pick your spot or press 'q' to quit")
    # Get input from payer
    choice = input()
    if choice.lower() == 'q':
        game_on = False
    # check if the player input is a number btw 1-9
    elif str.isdigit(choice) and int(choice) in choices:
        # Check if the number has already been taken
        if not choices[int(choice)] in {"X", "O"}:
            # Valid input
            turn += 1
            choices[int(choice)] = check_turn(turn)
        # print("That spot is already taken. Try again!")
        # Check if game has ended and if someone won

    if check_for_win(choices):
            game_on = False
            complete = True
    if turn > 8:
            game_on = False
            print(tie)

if complete:
    if check_turn(turn) == "X":
        print(player1)
        print(f"Congratulations {player_1}!!")
    else:
        print(player2)
        print(f"Congratulations {player_2}!!")







