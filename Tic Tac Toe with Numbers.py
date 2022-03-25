# Game: Tic Tac Toe with Numbers
# Name: Yusuf Badr | Student at the Faculty of Computers and Artificial Intelligence, Cairo University
# Email: yusufbadr@yahoo.com | LinkedIn: linkedin.com/in/yusufbadr/
# Version 3
# Date: 25/02/2022

from math import floor
from os import system, name
from time import sleep


def make_board():
    # returns a list containing 9 elements
    board = [' ' for x in range(9)]
    return board


def display_current_board(input_board):
    # prints the current board contents
    for index in range(0, 9,  3):  # inorder to print the board in a 3x3 format
        temp_board = input_board[index: index + 3]
        print(temp_board[0], "|", temp_board[1], "|", temp_board[2])


def display_welcome_message():
    print('''
Welcome to the 'Tic Tac Toe with Numbers' Game
Inorder to play, please type in the number that you wish to play with from your list of available numbers.
Then type in the letter corresponding to your desired position.

''')


def display_guidance_board():

    # prints to the user a 3x3 guidance board containing the letters which corresponds to the positions shown
    guidance_board = [x for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']]
    for index in range(0, 9,  3):
        temp_board = guidance_board[index: index + 3]
        print(temp_board[0] + " | " + temp_board[1] + " | " + temp_board[2])


def clear_the_screen():
    if name == 'nt':
        _ = system('cls')
    elif name == 'posix':
        _ = system('clear')


def make_move(index, input_number):
    global board
    board[index] = input_number


def get_index(letter):
    # returns the corresponding index (to be used in the board list) according to the letter received.
    # formula = ASCII of lower case letter received - ASCII of "a"
    letter = letter.lower()
    index = ord(letter) - 97
    return index


def generate_initial_available_moves():
    # returns a tuple containing two elements, such that the first element contains a list of available numbers for
    # player 1 and the second element contains a list of available numbers for player 2
    available_numbers_1 = [x for x in range(1, 11, 2)]
    available_numbers_2 = [x for x in range(0, 10, 2)]
    return available_numbers_1, available_numbers_2


def get_validated_input_number(moves_available_for_player):
    valid_input = False
    while valid_input is False:
        try:
            print("Please enter one the following numbers: ", moves_available_for_player, end='')
            number_chosen = int(input(": "))

            if number_chosen in moves_available_for_player:
                moves_available_for_player[int(number_chosen / 2)] = " "
                valid_input = True
            else:
                print("Wrong Input. Please try again.")

        except:
            print("Wrong Input. Please try again.")
    return number_chosen


def making_a_move(index, number):
    global board
    board[index] = number


def check_if_winner(player, index):
    # parameters: last player and their chosen position
    # returns False boolean value if no winner found till now, otherwise returns the player number who won

    # checking the row in which the player played in
    row_number = floor(index/3)  # possible values: 0, 1, 2
    temp_board_row = board[row_number * 3: row_number * 3 + 3]  # extracts the row in which the player played in
    sum_of_row = None

    try:
        sum_of_row = sum(temp_board_row)
    except:
        pass

    if sum_of_row is not None:
        if sum_of_row == 15:
            return player

    # checking the column in which the player played in
    column_number = index % 3  # possible values: 0, 1, 2
    temp_board_column = board[column_number: column_number + 7: 3]  # extracts the column in which the player played in
    sum_of_column = None
    try:
        sum_of_column = sum(temp_board_column)
    except:
        pass

    if sum_of_column is not None:
        if sum_of_column == 15:
            return player

    # checking diagonals
    if index % 2 == 0:
        # checking '/' diagonal
        try:
            if board[0] + board[4] + board[8] == 15:
                return player
        except:
            pass
        # checking '\' diagonal
        try:
            if board[2] + board[4] + board[6] == 15:
                return player
        except:
            pass

    return False


def play_game():
    global player
    display_welcome_message()
    display_guidance_board()
    moves_available = generate_initial_available_moves()
    available_letter_of_positions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    while True:
        player = 2 if player == 1 else 1  # alternates between player 1 and 2
        print("\n\nPlayer " + str(player) + "'s" + " turn. Please play your turn. ")
        moves_available_for_player = moves_available[player - 1]  # moves available for each player
        number_chosen = get_validated_input_number(moves_available_for_player)

        valid_input = False
        while valid_input is False:
            try:
                letter = input("Please enter the letter corresponding to your desired position: ")
                if len(letter) == 1 and ("a" <= letter <= "i" or "A" <= letter <= "I") and \
                        letter in available_letter_of_positions:
                    valid_input = True
                    available_letter_of_positions.remove(letter)


                else:
                    print("Wrong Input! Try again.")
            except:

                print("Wrong Input! Try again.")

        index = get_index(letter)
        making_a_move(index, number_chosen)
        display_current_board(board)

        is_winner = check_if_winner(player, index)
        if type(is_winner) != bool:
            print("Player", is_winner, "Won!")
            break

        if ' ' not in board:
            print("It's a draw")
            break

        sleep(1)
        clear_the_screen()
        display_guidance_board()
        print()
        display_current_board(board)


# main program starts here #
board = make_board()
player = " "
play_game()
print()
_ = input("Press enter to exit the terminal")  # holds the terminal

