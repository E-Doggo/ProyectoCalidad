
# Define the player colors
from utils import *


def terminal_test(board, player):

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


def find_adjacencies(board):
    number_b_adj = 0
    number_w_adj = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == BLACK:
                if board[i+1][j] == BLACK:
                    number_b_adj += 1
                if board[i-1][j] == BLACK:
                    number_b_adj += 1
                if board[i][j+1] == BLACK:
                    number_b_adj += 1
                if board[i][j-1] == BLACK:
                    number_b_adj += 1
                if board[i+1][j-1] == BLACK:
                    number_b_adj += 1
                if board[i+1][j+1] == BLACK:
                    number_b_adj += 1
                if board[i-1][j+1] == BLACK:
                    number_b_adj += 1
                if board[i-1][j-1] == BLACK:
                    number_b_adj += 1

            elif board[i][j] == WHITE:
                if board[i+1][j] == WHITE:
                    number_w_adj += 1
                if board[i-1][j] == WHITE:
                    number_w_adj += 1
                if board[i][j+1] == WHITE:
                    number_w_adj += 1
                if board[i][j-1] == WHITE:
                    number_w_adj += 1
    return number_b_adj, number_w_adj


def second_evaluation_function(state):
    board = state[0]
    weights = [[3, 2, 2, 3],
               [2, 1, 1, 2],
               [2, 1, 1, 2],
               [3, 2, 2, 3]]

    player1_score = 0
    player2_score = 0

    for i in range(4):
        for j in range(4):
            if board[i][j] == BLACK:
                player1_score += weights[i][j]
            elif board[i][j] == WHITE:
                player2_score += weights[i][j]

    adj1, adj2 = find_adjacencies(board)
    value = (player1_score-adj1) - (player2_score-adj2)
    return value


def get_all_moves(board, player):
    """
    Returns all available moves for a given player on the current board.
    """
    moves = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == EMPTY:
                # Check if the move would create a winning line
                temp_board = copy.deepcopy(board)
                temp_board[i][j] = player
                if terminal_test(temp_board, player) > 0:
                    moves.append((i, j))
                    continue

                # Check if the move would create a square
                if forms_square(temp_board, player):
                    moves.append((i, j))
                    continue

                # Check if the move would create a tile in every corner
                if forms_corners(temp_board, player):
                    moves.append((i, j))
                    continue

                # Otherwise, add the move to the list of available moves
                moves.append((i, j))

    return moves


def first_evaluation_function(state):
    board = state[0]

    weights = [[2, 2, 2, 2],
               [2, 1, 1, 2],
               [2, 1, 1, 2],
               [2, 2, 2, 2]]

    player1_score = 0
    player2_score = 0

    for i in range(4):
        for j in range(4):
            if board[i][j] == BLACK:
                player1_score += weights[i][j]
            elif board[i][j] == WHITE:
                player2_score += weights[i][j]

    player1_moves = len(get_all_moves(board, BLACK))
    player2_moves = len(get_all_moves(board, WHITE))

    value = player1_score - player2_score + \
        (player1_moves - player2_moves) * 0.1
    return value


def AlphaBetaPrunningDepth(state, depth, alpha, beta, maximizing_player, available_moves, counter):
    board = state[0]
    player = state[1]
    counter += 1

    if depth == 0 or (terminal_test(state[0], BLACK) > 0) or (terminal_test(state[0], WHITE) > 0):
        return second_evaluation_function(state), 0, counter
#       return first_evaluation_function(state), 0, counter

    if maximizing_player:
        max_value = float('-inf')
        best_move = None
        for move in available_moves:
            new_board = make_move(board, move, player)
            new_state = [new_board, get_opponent(player)]
            value, _, counter = AlphaBetaPrunningDepth(new_state, depth-1, alpha,
                                                       beta, False, available_moves, counter)
            if value > max_value:
                max_value = value
                best_move = move
            alpha = max(alpha, max_value)
            if beta <= alpha:
                break
        return max_value, best_move, counter

    else:
        min_value = float('inf')
        best_move = None
        for move in available_moves:
            new_board = make_move(board, move, player)
            new_state = [new_board, get_opponent(player)]
            value, _, counter = AlphaBetaPrunningDepth(new_state, depth-1, alpha,
                                                       beta, True, available_moves, counter)
            if value < min_value:
                min_value = value
                best_move = move
            beta = min(beta, min_value)
            if beta <= alpha:
                break
        return min_value, best_move, counter
