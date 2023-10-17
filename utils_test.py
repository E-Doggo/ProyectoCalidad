from utils import *
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

@pytest.fixture
def row_copy():
    return row_copy

@pytest.fixture
def col_copy():
    return col_copy
@pytest.fixture
def new_board():
    return [[None for _ in range(4)] for _ in range(4)]

@pytest.fixture
def previous_position():
    return previous_position

@pytest.fixture
def player():
    return player


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
    with pytest.raises(ValueError):
        make_move(empty_board, move_selected, player_black)

def test_make_move_failed_second_condition(empty_board, player_black):
    move_selected = "E2 N"
    with pytest.raises(ValueError):
        make_move(empty_board, move_selected, player_black)










def test_move_northwest_fails():
    row_copy=-100
    col_copy=-100
    new_board=[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]
    previous_position=0
    resulting_board = move_northwest(new_board, row_copy, col_copy, previous_position, player)
    assert resulting_board == ([None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None])


def test_northwest_all_true():
    row_copy=1
    col_copy=1
    new_board=['B',  None, None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None ]
    resulting_board = move_northwest(new_board, row_copy, col_copy, previous_position, player)
    assert resulting_board == (['B',  None, None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None])

def test_northwest_failed_second_condition():
    row_copy=1
    col_copy=1
    player=WHITE
    new_board=['W',  'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None ]
    resulting_board = move_northwest(new_board, row_copy, col_copy, previous_position, player)
    assert resulting_board == (['W', 'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None])

def test_northwest_failed_first_condition():
    row_copy = 3
    col_copy = -1
    player = WHITE
    new_board=([None, 'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None])
    resulting_board = move_northwest(new_board, row_copy, col_copy, previous_position, player)
    assert resulting_board == ([None, 'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None])












def test_move_north_fails():
    row_copy=-100
    col_copy=-100
    new_board=[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]
    previous_position=0
    resulting_board = move_north(new_board, row_copy, col_copy, previous_position, player)
    assert resulting_board == ([None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None])


def test_north_all_true():
    row_copy=1
    col_copy=1
    new_board=[ None,  'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None ]
    resulting_board = move_north(new_board, row_copy, col_copy, previous_position, player)
    assert resulting_board == ([None,  'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None])

def test_north_failed_second_condition():
    row_copy=1
    col_copy=1
    player=WHITE
    new_board=['W',  'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None ]
    resulting_board = move_north(new_board, row_copy, col_copy, previous_position, player)
    assert resulting_board == (['W', 'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None])

def test_north_failed_first_condition():
    row_copy = 3
    col_copy = -1
    player = WHITE
    new_board=([None, 'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None])
    resulting_board = move_north(new_board, row_copy, col_copy, previous_position, player)
    assert resulting_board == ([None, 'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None])










def test_move_west_fails():
    row_copy=-100
    col_copy=-100
    new_board=[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]
    previous_position=0
    resulting_board = move_west(new_board, row_copy, col_copy, previous_position, player)
    assert resulting_board == ([None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None])

def test_west_all_true():
    row_copy=1
    col_copy=1
    new_board=[None,  None, None, None], [['B', None, None, None]], [[None, None, None, None]], [None, None, None, None ]
    resulting_board = move_west(new_board, row_copy, col_copy, previous_position, player)
    assert resulting_board == ([None,  None, None, None], [['B', None, None, None]], [[None, None, None, None]], [None, None, None, None])

def test_west_failed_second_condition():
    row_copy=1
    col_copy=1
    player=WHITE
    new_board=['W',  'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None ]
    resulting_board = move_west(new_board, row_copy, col_copy, previous_position, player)
    assert resulting_board == (['W', 'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None])

def test_west_failed_first_condition():
    row_copy = 3
    col_copy = -1
    player = WHITE
    new_board=([None, 'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None])
    resulting_board = move_west(new_board, row_copy, col_copy, previous_position, player)
    assert resulting_board == ([None, 'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None])












def test_move_east_fails():
    row_copy=-100
    col_copy=-100
    new_board=[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]
    previous_position=0
    with pytest.raises(IndexError):
        move_east(new_board, row_copy, col_copy, previous_position, player)
def test_west_all_true():
    row_copy=1
    col_copy=1
    new_board=[None,  None, None, None], [['B', None, None, None]], [[None, None, None, None]], [None, None, None, None ]
    resulting_board = move_west(new_board, row_copy, col_copy, previous_position, player)
    assert resulting_board == ([None,  None, None, None], [['B', None, None, None]], [[None, None, None, None]], [None, None, None, None])

def test_west_failed_second_condition():
    row_copy=1
    col_copy=1
    player=WHITE
    new_board=['W',  'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None ]
    resulting_board = move_west(new_board, row_copy, col_copy, previous_position, player)
    assert resulting_board == (['W', 'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None])

def test_west_failed_first_condition():
    row_copy = 3
    col_copy = -1
    player = WHITE
    new_board=([None, 'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None])
    resulting_board = move_west(new_board, row_copy, col_copy, previous_position, player)
    assert resulting_board == ([None, 'B', None, None], [[None, None, None, None]], [[None, None, None, None]], [None, None, None, None])