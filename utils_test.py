from utils import *
import pytest

@pytest.fixture
def empty_board():
    #setup
    yield [[None for _ in range(4)] for _ in range(4)]
    #teardown


@pytest.fixture
def player_white():
    yield WHITE

@pytest.fixture
def player_black():
    yield BLACK

def test_traduction_move():
    move_string = "B2 N"
    row, column, direction = traduction_move(move_string)
    assert row == 1
    assert column == 1
    assert direction == "N"

def test_get_opponent_white(player_white):
    opponent = get_opponent(player_white)
    assert opponent == "B"

def test_get_opponent_black(player_black):
    opponent = get_opponent(player_black)
    assert opponent == "W"

def test_forms_corners_no_player(empty_board, player_white):
    result = forms_corners(empty_board, player_white)
    assert result == False

def test_forms_corners_3_corners(empty_board, player_white):
    board = empty_board
    player = player_white
    board[0][0] = player
    board[0][3] = player
    board[3][0] = player
    board[3][3] = get_opponent(player)
    result = forms_corners(board, player)
    assert  result == False

def test_forms_corners_all_corners(empty_board, player_white):
    board = empty_board
    player = player_white
    board[0][0] = player
    board[0][3] = player
    board[3][0] = player
    board[3][3] = player
    result = forms_corners(board, player)
    assert result == True

def test_make_move_succesfully(empty_board, player_black):
    move_selected = "A1 S"
    resulting_board = make_move(empty_board, move_selected ,player_black)
    assert resulting_board == [[None, None, None, None], [None, None, None, None], [None, None, None, None], ['B', None, None, None]]

def test_make_move_failed_first_condition(empty_board, player_black):
    move_selected = "B7 N"
    with pytest.raises(IndexError):
        make_move(empty_board, move_selected, player_black)

def test_make_move_failed_second_condition(empty_board, player_black):
    move_selected = "E2 N"
    with pytest.raises(IndexError):
        make_move(empty_board, move_selected, player_black)