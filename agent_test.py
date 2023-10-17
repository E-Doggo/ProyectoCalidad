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

def test_terminal_test_square_winner(empty_board, player_white, player_black):
    board = empty_board
    # Configura un ganador en un cuadrado
    board[0][0] = player_black
    board[0][1] = player_black
    board[1][0] = player_black
    board[1][1] = player_black
    assert terminal_test(board, player_black) == True

def test_terminal_test_no_winner(empty_board, player_white, player_black):
    board = empty_board
    # No hay ganador en este tablerocov
    assert terminal_test(board, player_black) == False

def test_find_adjacencies_case1(empty_board, player_white, player_black):
    # Caso de prueba para el camino 1: Inicio -> Fin
    board = empty_board
    result = find_adjacencies(board)
    assert result == (0, 0)

def test_find_adjacencies_case2(empty_board, player_white, player_black):
    # Caso de prueba para el camino 2: Inicio -> i loop -> Fin
    board = empty_board
    # Configura un valor en el tablero para activar el bucle i
    board[0][0] = player_white
    result = find_adjacencies(board)
    assert result == (0, -3)
def test_find_adjacencies_case3(empty_board, player_white, player_black):
    # Caso de prueba para el camino 3: Inicio -> i loop -> j loop -> Fin
    board = empty_board
    # Configura un valor en el tablero para activar ambos bucles i y j
    board[0][0] = player_white
    board[1][1] = player_black
    result = find_adjacencies(board)
    assert result == (8, -3)

def test_second_evaluation_function(empty_board, player_white, player_black):
    # Caso de prueba para cubrir el flujo básico de la función
    board = [
        [player_black, player_white, player_white, player_black],
        [player_white, player_black, player_black, player_white],
        [player_black, player_white, player_black, player_white],
        [player_white, player_black, player_white, player_black]
    ]
    state = (board,)
    result = second_evaluation_function(state)
    assert result == -40  