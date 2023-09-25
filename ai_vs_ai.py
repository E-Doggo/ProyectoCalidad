import time
import random
from utils import *
from agent import AlphaBetaPrunningDepth

def create_board():
    board = [[None for j in range(4)] for i in range(4)]
    board[0][0] = 'B'
    board[0][3] = 'W'
    board[1][1] = 'B'
    board[1][2] = 'W'
    board[2][1] = 'W'
    board[2][2] = 'B'
    board[3][0] = 'W'
    board[3][3] = 'B'
    return board


# Define the function for checking if a player has won

def check_win(board, player):

    for i in range(4):
        if board[i] == [player, player, player, player]:
            return True

    for j in range(4):
        if [board[x][j] for x in range(4)] == [player, player, player, player]:
            return True

    if board[0][0] == player and board[0][3] == player and board[3][0] == player and board[3][3] == player:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == player and board[i][j+1] == player and board[i+1][j] == player and board[i+1][j+1] == player:
                return True

    return False
# Define the function for displaying the game board


def display_board(board):
    print('   A   B   C   D')
    print('1  {} | {} | {} | {}'.format(
        board[0][0] or ' ', board[0][1] or ' ', board[0][2] or ' ', board[0][3] or ' '))
    print('  ---|---|---|---')
    print('2  {} | {} | {} | {}'.format(
        board[1][0] or ' ', board[1][1] or ' ', board[1][2] or ' ', board[1][3] or ' '))
    print('  ---|---|---|---')
    print('3  {} | {} | {} | {}'.format(
        board[2][0] or ' ', board[2][1] or ' ', board[2][2] or ' ', board[2][3] or ' '))
    print('  ---|---|---|---')
    print('4  {} | {} | {} | {}'.format(
        board[3][0] or ' ', board[3][1] or ' ', board[3][2] or ' ', board[3][3] or ' '))


def is_possible_move(direction, row, col, board, player):
    if (direction == 'N' and row == 0) or (direction == 'S' and row == len(board)-1) or \
       (direction == 'W' and col == 0) or (direction == 'E' and col == len(board[0])-1):
        return False
    if (direction == 'NW' and (row == 0 or col == 0)) or \
       (direction == 'NE' and (row == 0 or col == len(board[0])-1)) or \
       (direction == 'SW' and (row == len(board)-1 or col == 0)) or \
       (direction == 'SE' and (row == len(board)-1 or col == len(board[0])-1)):
        return False

    # Verificar que no haya otra ficha del mismo jugador en la casilla a la que se quiere mover
    if direction == 'N' and (board[row-1][col] == player or board[row-1][col] == get_opponent(player)):
        return False
    if direction == 'S' and (board[row+1][col] == player or board[row+1][col] == get_opponent(player)):
        return False
    if direction == 'W' and (board[row][col-1] == player or board[row][col-1] == get_opponent(player)):
        return False
    if direction == 'E' and (board[row][col+1] == player or board[row][col+1] == get_opponent(player)):
        return False
    if direction == 'NW' and (board[row-1][col-1] == player or board[row-1][col-1] == get_opponent(player)):
        return False
    if direction == 'NE' and (board[row-1][col+1] == player or board[row-1][col+1] == get_opponent(player)):
        return False
    if direction == 'SW' and (board[row+1][col-1] == player or board[row+1][col-1] == get_opponent(player)):
        return False
    if direction == 'SE' and (board[row+1][col+1] == player or board[row+1][col+1] == get_opponent(player)):
        return False

    return True


def get_computer_move(state,eva_type):
    board = state[0]
    player = state[1]
    available_moves = []
    counter = 0

    for i in range(4):
        for j in range(4):
            if board[i][j] == player:
                for direction in ['N', 'S', 'E', 'W', 'NW', 'NE', 'SW', 'SE']:

                    move = f"{chr(ord('A') + j)}{i+1} {direction}"
                    row, col, direction = traduction_move(move)
                    if (is_possible_move(direction, row, col, board, player)):
                        available_moves.append(move)

    if not available_moves:
        return None

    max_depth = 3
    _, best_move, counter = AlphaBetaPrunningDepth(state, max_depth, float(
        '-inf'), float('inf'), True, available_moves, counter, eva_type)
    print("Number of states expanded: ", counter)
    return best_move


# Define the function for playing the game


def play_game():
    board = create_board()
    display_board(board)

    a1 = random.choice([BLACK, WHITE])

    if a1 == BLACK:
        a2 = WHITE
    else:
        a2 = BLACK

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


play_game()
