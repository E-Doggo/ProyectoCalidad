from game import *
import pytest

@pytest.fixture
def empty_board():
    #setup
    yield [[None for _ in range(4)] for _ in range(4)]
    #teardown


@pytest.fixture
def create_state():
    board = create_board()
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

def test_check_win_3(empty_board):
    board = empty_board
    board [0][0] = BLACK
    board [0][3] = BLACK  
    board [3][0] = BLACK
    board [3][3] = BLACK
    result = check_win(board, BLACK)
    assert result == True


def test_check_win_4(empty_board):
    board = empty_board
    result = check_win(board, BLACK)
    assert result == False

def test_display_board(capsys):
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
    )

    expected_output = captured.out

    assert captured.out == expected_output

def test_get_user_move_valid_move(create_state, capsys, monkeypatch):
    state = create_state

    user_input = "A1 S"

    monkeypatch.setattr('builtins.input', lambda _: user_input)

    with capsys.disabled():
        result = get_user_move(state)

    assert result == (True, 'A1 S')



def test_get_user_move_invalid_move(create_state, capsys, monkeypatch):
    state = create_state

    user_input = "A2 E"

    monkeypatch.setattr('builtins.input', lambda _: user_input)
    
    with capsys.disabled():
        result = get_user_move(state)

    assert result == (False, 0)

def test_get_user_move_wrong_piece(create_state, capsys, monkeypatch):
    state = create_state

    user_input = "D1 S"

    monkeypatch.setattr('builtins.input', lambda _: user_input)
    
    with capsys.disabled():
        result = get_user_move(state)

    assert result == (False, 0)  

def test_get_computer_move(create_state):
    state = create_state
    
    result = get_computer_move(state, 1)

    assert result == 'B2 N'