import time
import random
from utils import make_move, get_opponent, BLACK, WHITE, EMPTY
from game import create_board, check_win, display_board, get_computer_move
import secrets
def choose_starting_player():
    return secrets.choice([BLACK, WHITE])

def play_ai_game():
    board = create_board()
    display_board(board)

    a1 = choose_starting_player()

    player = BLACK  # set player to always be black
    state = (board, player)
    move = None
    while not check_win(board, BLACK) and not check_win(board, WHITE):
        if player == a1:
            move = get_computer_move(state, 1)
            print("Computer's move: ", move)
            board = make_move(board, move, player)

            state = (board, get_opponent(player))
            display_board(board)

        else:
            move = get_computer_move(state, 2)
            print("Computer's move: ", move)

        try:
            board = make_move(board, move, player)

            state = (board, get_opponent(player))
            display_board(board)
        except ValueError as e:
            print(e)

        player = get_opponent(player)

    print('Game over! Winner: ', get_opponent(player))


if __name__ == "__main__":
    play_ai_game()  
