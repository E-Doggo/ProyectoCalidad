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
