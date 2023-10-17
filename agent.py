
# Define the player colors
from utils import make_move, get_opponent, BLACK, WHITE, EMPTY, forms_corners, forms_square
import copy

#Move to utils
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

#Move to utils
def find_adjacencies(board):
    adjecencies = {BLACK:0, WHITE:0}
    values = {BLACK:1, WHITE:-1}

   # Define the offsets for adjacent cells
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(3):
        for j in range(3):
                for offset_i, offset_j in offsets:
                    color = board[i + offset_i][j + offset_j]
                    if 0 <= i + offset_i < 3 and 0 <= j + offset_j < 3 and color != EMPTY and color != None: 
                        adjecencies[color] += values[color]

    return adjecencies[BLACK], adjecencies[WHITE]

#Move to utils
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

#Move to utils
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
                if terminal_test(temp_board, player) > 0 or forms_square(temp_board, player) or forms_corners(temp_board, player):
                    moves.append((i, j))
                    continue

                # Otherwise, add the move to the list of available moves
                moves.append((i, j))

    return moves

#Move to utils
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


def alpha_beta_prunning_depth(state, depth, alpha, beta, maximizing_player, available_moves, counter, eva_type):
    board = state[0]
    player = state[1]
    counter += 1
    best_move = None
    evaluations={1:first_evaluation_function, 2:second_evaluation_function}

    val = float('inf')
    if maximizing_player:
        val = float('-inf')

    if depth == 0 or (terminal_test(state[0], BLACK) > 0) or (terminal_test(state[0], WHITE) > 0):
        return evaluations[eva_type](state), 0, counter

    for move in available_moves:
        new_board = make_move(board, move, player)
        new_state = [new_board, get_opponent(player)]
        new_value, _, counter = alpha_beta_prunning_depth(new_state, depth-1, alpha,
                                                beta, not maximizing_player, available_moves, counter,eva_type)
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
    return val, best_move, counter
def test_first_evaluation_function_case1(empty_board, player_white, player_black):
    # Caminos 1, 2, 3, 4, 5, 6, 7: Inicio -> Fin
    board = empty_board
    state = (board,)
    result = first_evaluation_function(state)
    assert result == 0  # Puedes ajustar el valor esperado según tus necesidades