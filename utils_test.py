from utils import *
import pytest

@pytest.fixture
def create_empty_board():
    board = [[None for _ in range(4)] for _ in range(4)]
    return board

@pytest.fixture
def create_player_white():
    return WHITE
     

@pytest.fixture
def create_player_black():
    return BLACK

#traduction_move test: complejidad ciclomatica 1
def test_traduction_move():
    move_string = "B2 N"
    row, column, direction = traduction_move(move_string)
    assert row == 1
    assert column == 1
    assert direction == "N"
    

#traduction_move test: complejidad ciclomatica 2
def test_get_opponent_White(create_player_white):
    player = create_player_white
    opponent = get_opponent(player)
    assert opponent == "B"

def test_get_opponent_Black(create_player_black):
    player = create_player_black

    opponent = get_opponent(player)
    assert opponent == "W"

def test_forms_corners_no_player(create_empty_board, create_player_white):
    board = create_empty_board
    player = create_player_white
    result = forms_corners(board, player)
    assert result == False

def test_forms_corners_3_corners(create_empty_board, create_player_white):
    board = create_empty_board
    player = create_player_white
    board[0][0] = player
    board[0][3] = player
    board[3][0] = player
    board[3][3] = get_opponent(player)
    result = forms_corners(board, player)
    assert result == False

def test_forms_corners_all_corners(create_empty_board, create_player_white):
    board = create_empty_board
    player = create_player_white
    board[0][0] = player
    board[0][3] = player
    board[3][0] = player
    board[3][3] = player
    result = forms_corners(board, player)
    assert result == True