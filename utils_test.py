from utils import *

def test_traduction_move():
    move_string = "B2 N"
    row, column, direction = traduction_move(move_string)
    assert row == 1
    assert column == 1
    assert direction == "N"
    

def test_get_opponent_White():
    player = "W"
    opponent = get_opponent(player)
    assert opponent == "B"

def test_get_opponent_Black(): 
    player = "B"
    opponent = get_opponent(player)
    assert opponent == "W"