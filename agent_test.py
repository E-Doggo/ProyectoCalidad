from agent import *
import pytest 

@pytest.fixture
def empty_board():
    return [[None for _ in range(4)] for _ in range(4)]

@pytest.fixture
def player_white():
    return WHITE

@pytest.fixture
def player_black():
    return BLACK

def test_terminal_test_horizontal_winner(empty_board, player_white):
    board = empty_board
    # Configura un ganador en una fila horizontal
    board[0] = [player_white, player_white, player_white, player_white]
    assert terminal_test(board, player_white) == True

def test_terminal_test_vertical_winner(empty_board, player_white, player_black):
    board = empty_board
    # Configura un ganador en una columna vertical
    for i in range(4):
        board[i][0] = player_black
    assert terminal_test(board, player_black) == True