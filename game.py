import time
import random
from agent import alpha_beta_prunning_depth
from agent_no_cutoff import alpha_beta_prunning
from utils import make_move, get_opponent,traduction_move, BLACK, WHITE, EMPTY


def create_board():
    board = [[None for _ in range(4)] for _ in range(4)]
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
    for i in range(4):
        row = '{}  {} | {} | {} | {}'.format(i + 1, *(board[i][j] or ' ' for j in range(4)))
        separator = '  ---|---|---|---' if i < 3 else ''
        print(row + '\n'+separator)


def get_user_move(state):
    board = state[0]
    player = state[1]

    while True:
        try:
            move_str = input('Enter your move (e.g., C2 SE): ')
            col, row, _ = traduction_move(move_str.upper())
            if board[col][row] == None or board[col][row] == get_opponent(player):
                return False, 0
            return True, move_str.upper()
        except ValueError:
            print('Invalid move. Please try again.')


def is_possible_move(direction, row, col, board, player):
    rows, cols = len(board), len(board[0])

    # Define directional offsets
    direction_offsets = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1),
        'NW': (-1, -1),
        'NE': (-1, 1),
        'SW': (1, -1),
        'SE': (1, 1),
    }

    # Check if the move is within the board boundaries
    row_offset, col_offset = direction_offsets.get(direction, (0, 0))
    new_row, new_col = row + row_offset, col + col_offset

    if not (0 <= new_row < rows and 0 <= new_col < cols):
        return False

    # Check if the target cell is already occupied by the same or opposite player
    target_cell = board[new_row][new_col]

    if target_cell in (player, get_opponent(player)):
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
    _, best_move, counter = alpha_beta_prunning_depth(state, max_depth, float(
        '-inf'), float('inf'), True, available_moves, counter, eva_type)
    print("Number of states expanded: ", counter)
    return best_move


def get_computer_move_no_cutoff(state):
    board = state[0]
    player = state[1]
    available_moves = []

    for i in range(4):
        for j in range(4):
            if board[i][j] == player:
                for direction in ['N', 'S', 'E', 'W', 'NW', 'NE', 'SW', 'SE']:
                    move = f"{chr(ord('A') + j)}{i+1} {direction}"
                    available_moves.append(move)

    if not available_moves:
        return None

    _, best_move = alpha_beta_prunning(state, float(
        '-inf'), float('inf'), True, available_moves)
    return best_move


# Define the function for playing the game


def play_game():
    board = create_board()
    display_board(board)

    human_player = None
    while human_player not in [BLACK, WHITE]:
        try:
            human_player = input(
                "Choose your color ('B' for Black, 'W' for White): ").upper()
        except ValueError:
            print('Invalid input. Please try again.')
    player = WHITE  # set player to always be black
    state = (board, player)

    while not check_win(board, BLACK) and not check_win(board, WHITE):
        mov_valido = False
        if player == human_player:
            while (mov_valido == False):
                mov_valido, move = get_user_move(state)
        else:
            move = get_computer_move(state,1)
            print("Computer's move: ", move)

        try:
            board = make_move(board, move, player)

            state = (board, get_opponent(player))
            display_board(board)
        except ValueError as e:
            print(e)

        player = get_opponent(player)

    print('Game over! Winner: ', get_opponent(player))


def play_game_no_cutoff():
    board = create_board()
    display_board(board)

    human_player = None
    while human_player not in [BLACK, WHITE]:
        try:
            human_player = input(
                "Choose your color ('B' for Black, 'W' for White): ").upper()
        except ValueError:
            print('Invalid input. Please try again.')

    if human_player == BLACK:
        computer_player = WHITE
    else:
        computer_player = BLACK

    player = computer_player  # set player to always be black
    state = (board, player)

    while not check_win(board, BLACK) and not check_win(board, WHITE):
        mov_valido = False
        if player == human_player:
            while (mov_valido == False):
                mov_valido, move = get_user_move(state)
        else:
            move = get_computer_move_no_cutoff(state)
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
    play_game()

