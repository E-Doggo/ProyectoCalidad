import time
import random
import sys
from utils import make_move, BLACK, WHITE, get_opponent
from agent import terminal_test


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

    for move in available_moves:
        new_board = make_move(board, move, player)
        new_state = [new_board, get_opponent(player)]
        new_value, _ = AlphaBetaPrunning(new_state, alpha,
                                                beta, not maximizing_player, available_moves)
        if maximizing_player:
            if new_value > val:
                val = new_value
                best_move = move
            alpha = max(alpha, val)
        else:
            if new_value < val:
                val = new_value
                best_move = move
            beta = min(beta, val)
        if beta <= alpha:
                break
    return val, best_move
