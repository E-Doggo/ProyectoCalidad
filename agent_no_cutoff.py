import time
import random
import sys
from utils import make_move, BLACK, WHITE, get_opponent


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
                if board[i+1][j-1] == WHITE:
                    number_w_adj += 1
                if board[i+1][j+1] == WHITE:
                    number_w_adj += 1
                if board[i-1][j+1] == WHITE:
                    number_w_adj += 1
                if board[i-1][j-1] == WHITE:
                    number_w_adj += 1

    return number_b_adj, number_w_adj


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


def utility(state):
    opponent = get_opponent(state[1])
    if terminal_test(state[0], state[1]):
        return 100
    elif terminal_test(state[1], opponent):
        return -100
    else:
        return 0


def AlphaBetaPrunning(state, alpha, beta, maximizing_player, available_moves):
    board = state[0]
    player = state[1]

    if (terminal_test(state[0], BLACK)) or (terminal_test(state[0], WHITE)):
        return utility(state), 0

    if maximizing_player:
        max_value = float('-inf')
        best_move = None
        for move in available_moves:
            new_board = make_move(board, move, player)
            new_state = [new_board, get_opponent(player)]
            value, _ = AlphaBetaPrunning(new_state, alpha,
                                         beta, False, available_moves)
            if value > max_value:
                max_value = value
                best_move = move
            alpha = max(alpha, max_value)
            if beta <= alpha:
                print(board)

        return max_value, best_move

    else:
        min_value = float('inf')
        best_move = None
        for move in available_moves:
            new_board = make_move(board, move, player)
            new_state = [new_board, get_opponent(player)]
            value, _ = AlphaBetaPrunning(new_state, alpha,
                                         beta, True, available_moves)
            if value < min_value:
                min_value = value
                best_move = move
            beta = min(beta, min_value)
            if beta <= alpha:
                print(board)

        return min_value, best_move
