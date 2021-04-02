import pytest
from ex48 import lexicon

def test_game_lexicon():
    test_keys = ['direction', 'verb', 'stop', 'numbers']
    test_values = [['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
                   ['go', 'stop', 'kill', 'eat'],
                   ['the', 'in', 'of', 'from', 'at', 'it'],
                   [i for i in range(0, 10)]]

    # Checking to see if the dictionary matched
    count = 0
    for key, value in lexicon.game_lexicon.items():
        assert key == test_keys[count]
        assert value == test_values[count]
        count += 1

    # Checking the integers are within 0-9
    assert max(lexicon.game_lexicon.get("numbers")) == 9
    assert min(lexicon.game_lexicon.get("numbers")) == 0

def test_getTag():
    """
    Testing out the getTag function.
    First, see if it returns the tuple    ----> return (token, word)
    Second, test if the word parsed is not in the lexicon ---> return none
    Third, test if unknown variables are paresed (e.g. list)
    """
    assert lexicon.getTag('north', lexicon.game_lexicon) == ('direction', 'north')
    assert lexicon.getTag('North', lexicon.game_lexicon) == ('direction', 'North')
    assert lexicon.getTag('Spencer', lexicon.game_lexicon) == ('noun', 'Spencer')
    assert lexicon.getTag(5, lexicon.game_lexicon) == ('number', 5)
    assert lexicon.getTag([5432,6453,78653,368], lexicon.game_lexicon) == ('error', [5432,6453,78653,368])
