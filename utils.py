# Define the player colors
BLACK = 'B'
WHITE = 'W'
EMPTY = ' '


def traduction_move(move):
    col = ord(move[0]) - ord('A')
    row = int(move[1]) - 1
    direction = move[3:]
    return row, col, direction


def get_opponent(player):
    if player == BLACK:
        return WHITE
    else:
        return BLACK


# Define the function for making a move on the board

def directions_to_move(direction, new_board, row_copy, col_copy, previous_position, player):
    if direction == 'NW':
        for n in range(1, min(row_copy+1, col_copy+1)+1):
            if row_copy-n >= 0 and col_copy >= 0:
                if new_board[row_copy-n][col_copy-n] is not None:
                    break
                new_board[row_copy-n][col_copy-n] = player
                new_board[previous_position[0]][previous_position[1]] = None
                previous_position = [row_copy-n, col_copy-n]

    elif direction == 'N':
        for n in range(1, row_copy+1):
            if row_copy-n >= 0:
                if new_board[row_copy-n][col_copy] is not None:
                    break
                new_board[row_copy-n][col_copy] = player
                new_board[previous_position[0]][previous_position[1]] = None
                previous_position = [row_copy-n, col_copy]

    elif direction == 'NE':
        for n in range(1, min(row_copy+1, 4-col_copy)+1):
            if row_copy-n >= 0 and col_copy+n < 4:
                if new_board[row_copy-n][col_copy+n] is not None:
                    break
                new_board[row_copy-n][col_copy+n] = player
                new_board[previous_position[0]][previous_position[1]] = None
                previous_position = [row_copy-n, col_copy+n]

    elif direction == 'W':
        for n in range(1, col_copy+1):
            if col_copy-n >= 0:
                if new_board[row_copy][col_copy-n] is not None:
                    break
                new_board[row_copy][col_copy-n] = player
                new_board[previous_position[0]][previous_position[1]] = None
                previous_position = [row_copy, col_copy-n]

    elif direction == 'E':
        for n in range(1, 4-col_copy):
            if col_copy+n < 4:
                if new_board[row_copy][col_copy+n] is not None:
                    break
                new_board[row_copy][col_copy+n] = player
                new_board[previous_position[0]][previous_position[1]] = None
                previous_position = [row_copy, col_copy+n]

    elif direction == 'SW':
        for n in range(1, min(4-row_copy, col_copy+1)+1):
            if row_copy+n < 4 and col_copy-n > 0:
                if new_board[row_copy+n][col_copy-n] is not None:
                    break
                new_board[row_copy+n][col_copy-n] = player
                new_board[previous_position[0]][previous_position[1]] = None
                previous_position = [row_copy+n, col_copy-n]

    elif direction == 'S':
        for n in range(1, 4-row_copy):
            if row_copy+n < 4:
                if new_board[row_copy+n][col_copy] is not None:
                    break
                new_board[row_copy+n][col_copy] = player
                new_board[previous_position[0]][previous_position[1]] = None
                previous_position = [row_copy+n, col_copy]

    elif direction == 'SE':
        for n in range(1, min(4-row_copy, 4-col_copy)+1):
            if row_copy+n < 4 and col_copy+n < 4:
                if new_board[row_copy+n][col_copy+n] is not None:
                    break
                new_board[row_copy+n][col_copy+n] = player
                new_board[previous_position[0]][previous_position[1]] = None
                previous_position = [row_copy+n, col_copy+n]
    return new_board


def make_move(board, move, player):
    row, col, direction = traduction_move(move)
    row_copy, col_copy = row, col
    previous_position = [row_copy, col_copy]

    if row_copy < 0 or row_copy > 3 or col_copy < 0 or col_copy > 3:
        raise ValueError(
            "Invalid move: position out of range ")

    new_board = [row[:] for row in board]

    return directions_to_move(direction, new_board, row_copy, col_copy, previous_position, player)


def forms_corners(board, player):

    corners = [(0, 0), (0, 3), (3, 0), (3, 3)]
    for corner in corners:
        if board[corner[0]][corner[1]] != player:
            return False
    return True


def forms_square(board, player):
    # Check horizontal squares
    for i in range(3):
        for j in range(3):
            if board[i][j] == player and board[i][j+1] == player and \
                    board[i+1][j] == player and board[i+1][j+1] == player:
                return True

    # Check vertical squares
    for i in range(3):
        for j in range(3):
            if board[i][j] == player and board[i+1][j] == player and \
                    board[i][j+1] == player and board[i+1][j+1] == player:
                return True

    # Check diagonal squares
    if board[0][0] == player and board[1][1] == player and \
            board[0][1] == player and board[1][0] == player:
        return True
    if board[0][2] == player and board[1][1] == player and \
            board[0][3] == player and board[1][2] == player:
        return True
    if board[1][0] == player and board[2][1] == player and \
            board[1][1] == player and board[2][0] == player:
        return True
    if board[1][2] == player and board[2][1] == player and \
            board[1][3] == player and board[2][2] == player:
        return True
    if board[2][0] == player and board[3][1] == player and \
            board[2][1] == player and board[3][0] == player:
        return True
    if board[2][2] == player and board[3][1] == player and \
            board[2][3] == player and board[3][2] == player:
        return True

    return False
