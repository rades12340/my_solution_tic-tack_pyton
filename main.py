from IPython.display import clear_output
import sys

test_table = [" "] * 10


def display_board(board):
    clear_output()
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-|-|-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-|-|-")
    print(board[1] + "|" + board[2] + "|" + board[3])


def check_won(mark, board):
    if (board[1] == board[2] == board[3] == mark or
            board[4] == board[5] == board[6] == mark or
            board[4] == board[5] == board[6] == mark or
            board[1] == board[5] == board[9] == mark or
            board[3] == board[5] == board[7] == mark or
            board[1] == board[4] == board[7] == mark or
            board[2] == board[5] == board[8] == mark or
            board[3] == board[6] == board[9] == mark):
        return True
    else:
        return False


def player_input():
    marker = ""

    while marker != "X" and marker != "O":
        marker = input('Player 1, choose X or O: ').upper()

    player1 = marker

    if player1 == 'X':
        player2 = "O"
    else:
        player2 = "X"

    return (player1, player2)





def want_to_play():
    value = input("Are you sure wanna play? Enter Y or N? ").upper()
    if value == 'Y':
        return True
    else:
        print('Thank you for playing')
        sys.exit()


def replay():
    value = input("Would you like to play again? Enter 'y' for yes or 'n' for no ").upper()
    if value == 'Y':

        return True
    else:
        print('Thank you for playing')
        sys.exit()

def adding_marker():
    user1, user2 = player_input()
    current_user = user1
    while (not check_won(current_user, test_table) and " " in test_table[1:]):
        marker = int(input(f'Please enter a field of {current_user} user? '))
        test_table[marker] = current_user
        display_board(test_table)
        if check_won(current_user, test_table):
            display_board(test_table)
            print(f'Player {current_user} won a game')
            want_to_play()
            confirm = replay()
            if confirm:
                for i in range(1, 9):
                    test_table[i] = ' '
                adding_marker()
                break
            else:
                print('Thank you for playing')
                sys.exit()
        if (" " not in test_table[1:]):
            print('Its tie, no winner')
            want_to_play()
            confirm = replay()
            if confirm:
                for i in range(0, 10):
                    test_table[i] = ' '
                adding_marker()
                break
            else:
                print('Thank you for playing')
                sys.exit()
        if current_user == 'X':
            current_user = "O"
        else:
            current_user = "X"

adding_marker()
