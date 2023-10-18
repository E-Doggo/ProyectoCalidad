from game import *
import pytest
from unittest.mock import patch


@pytest.fixture
def empty_board():
    #setup
    yield [[None for _ in range(4)] for _ in range(4)]
    #teardown


@pytest.fixture
def create_state_black():
    board = create_board()
    player = BLACK
    state = [board, player]
    yield state
    state = None

@pytest.fixture
def create_state_white():
    board = create_board()
    player = WHITE
    state = [board, player]
    yield state
    state = None

@pytest.fixture
def create_state_with_empty_board(empty_board):
    board = empty_board
    player = BLACK
    state = [board, player]
    yield state
    state = None



def test_create_board():
    board = create_board()
    assert board == [['B',None,None,'W'],[None,'B', 'W', None],[None, 'W', 'B', None],['W', None, None, 'B']]

def test_check_win_1(empty_board):
    board = empty_board
    for i in range(4):
        board [0][i] = BLACK
    result = check_win(board, BLACK)
    assert result == True


def test_check_win_2(empty_board):
    board = empty_board
    for i in range(4):
        board [i][0] = BLACK
    result = check_win(board, BLACK)
    assert result == True

test_data = [
    (True, [[BLACK, None, None, BLACK], [None, None, None, None], [None, None, None, None], [BLACK, None, None, BLACK]]),
    (False, [[BLACK, None, None, BLACK], [None, None, None, None], [None, None, None, None], [BLACK, None, None, WHITE]]),
    (False, [[BLACK, None, None, BLACK], [None, None, None, None], [None, None, None, None], [WHITE, None, None, BLACK]]),
    (False, [[BLACK, None, None, WHITE], [None, None, None, None], [None, None, None, None], [BLACK, None, None, BLACK]]),
    (False, [[WHITE, None, None, BLACK], [None, None, None, None], [None, None, None, None], [BLACK, None, None, BLACK]]),
]

@pytest.mark.parametrize("expected_result, board", test_data)
def test_check_win(empty_board, expected_result, board):
    empty_board[:] = board
    result = check_win(empty_board, BLACK)
    assert result == expected_result


def test_check_win_8(empty_board):
    board = empty_board
    result = check_win(board, BLACK)
    assert result == False

def test_display_board_success(capsys):
    sample_board = create_board()
    display_board(sample_board)

    captured = capsys.readouterr()

    expected_output = (
    "   A   B   C   D"
    "1  B |   |   | W"
    "  ---|---|---|---"
    "2    | B | W |  "
    "  ---|---|---|---"
    "3    | W | B |  "
    "  ---|---|---|---"
    "4  W |   |   | B"
    "  ---|---|---|---"
    )

    expected_output = captured.out

    assert captured.out == expected_output
    
def test_display_board_failure():
    with pytest.raises(TypeError):
        display_board()



def test_is_possible_move_true(create_state_black):
    state = create_state_black
    row, column, direction = traduction_move('A1 S')
    result = is_possible_move(direction, row, column, state[0], state[1])
    assert result == True

def test_is_possible_move_false_1(create_state_black):
    state = create_state_black
    row, column, direction = traduction_move('D1 N')
    result = is_possible_move(direction, row, column, state[0], state[1])
    assert result == False


def test_is_possible_move_false_2(create_state_black):
    state = create_state_black
    row, column, direction = traduction_move('F1 E')
    result = is_possible_move(direction, row, column, state[0], state[1])
    assert result == False


def test_is_possible_move_false_4(create_state_black):
    state = create_state_black
    row, column, direction = traduction_move('A5 N')
    result = is_possible_move(direction, row, column, state[0], state[1])
    assert result == False

valid_moves = [
    ("A1 S", (True, "A1 S")),
]

invalid_moves = [
    ("A2 E", (False, 0)),
    ("D1 S", (False, 0)),
]

@pytest.mark.parametrize("user_input, expected_result", valid_moves)
def test_get_user_move_valid_move(create_state_black, capsys, monkeypatch, user_input, expected_result):
    state = create_state_black
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    
    with capsys.disabled():
        result = get_user_move(state)
    
    assert result == expected_result

@pytest.mark.parametrize("user_input, expected_result", invalid_moves)
def test_get_user_move_invalid_move(create_state_black, capsys, monkeypatch, user_input, expected_result):
    state = create_state_black
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    
    with capsys.disabled():
        result = get_user_move(state)
    
    assert result == expected_result



def test_get_computer_move(create_state_white):
    state = create_state_white
    
    result = get_computer_move(state, 1)

    assert result == 'D1 S'

def test_get_computer_move_no_moves():
    board = [['B','B','B',None],['B','W', 'B', None],['B', 'B', 'B', None],[None, None, None, None]]
    state = [board, WHITE]
    
    result = get_computer_move(state, 1)

    assert result == None


def test_get_computer_move_no_players(create_state_with_empty_board):
    state = create_state_with_empty_board
    
    result = get_computer_move(state, 1)

    assert result == None
 

def test_get_computer_move_void_board():
    state = [[],WHITE]
    
    with pytest.raises(IndexError):
        get_computer_move(state,1)


def test_get_computer_move_no_parameters():
    
    with pytest.raises(TypeError):
        get_computer_move()


def test_get_computer_nocutoff_move(create_state_white):
    state = create_state_white
    with pytest.raises(RecursionError):
        get_computer_move_no_cutoff(state)


def test_get_computer_move_nocutoff_no_moves():
    board = [['B','B','B',None],['B','W', 'B', None],['B', 'B', 'B', None],[None, None, None, None]]
    state = [board, WHITE]
    
    result = get_computer_move_no_cutoff(state)

    assert result == None



def test_get_computer_move_nocutoff_no_players(create_state_with_empty_board):
    state = create_state_with_empty_board
    
    result = get_computer_move_no_cutoff(state)

    assert result == None



def test_get_computer_move_nocutoff_void_board():
    state = [[],WHITE]
    
    with pytest.raises(IndexError):
        get_computer_move_no_cutoff(state)


def test_get_computer_move_nocutoff_no_parameters():
    
    with pytest.raises(TypeError):
        get_computer_move_no_cutoff()



def custom_input(prompt):
    try:
        return next(custom_input.iterator)
    except StopIteration:
        raise StopIteration("No more input values provided")

custom_input.iterator = iter([])

@pytest.mark.parametrize("user_input, moves, expected_winner", [
    ("B\n", ['C1 N', 'B2 S', 'W3 E', 'C4 SW', 'W4 NE', 'B1 N', 'W2 S', 'C3 E', 'B4 SW', 'W1 N', 'C2 S', 'B3 E', 'W1 N'], "BLACK"),
    ("W\n", ['B1 N', 'W2 S', 'C3 E', 'B4 SW', 'W1 N', 'C2 S', 'B3 E', 'W1 N', 'C1 N', 'B2 S', 'W3 E', 'C4 SW', 'B1 N'], "WHITE"),
])
def test_play_game(user_input, moves, expected_winner, capsys):
    # Use the custom_input function for input
    custom_input.iterator = iter(user_input.split('\n')[:-1])

    # Set up the sequences of moves
    moves_input = '\n'.join(moves)

    # Capture the standard output
    with patch('builtins.input', custom_input):
        with patch('builtins.print') as mock_print:
            with pytest.raises(StopIteration):
                play_game()