import pytest
from ex49.parser import *

# Setting up one list of tuples for testing
peekList = [
        ('noun', 'bear'),
        ('verb', 'eat'),
        ('stop', 'the'),
        ('noun', 'honey')
        ]

peekList2 = [
        ('noun', 'I'),
        ('verb', 'want'),
        ('stop', 'to'),
        ('noun', 'drink some water')
        ]

errorSentence = [
            ('noun', 'Busque'),
            ('noun', 'Apple'),
            ('verb', 'eat'),
            ('stop', 'to')
            ]

def test_parse_sentence():
    """
    Using the test cases in the exercise below
    """
    x = parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert x.subject == 'player'
    assert x.verb == 'run'
    assert x.object == 'north'

    y = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
    assert y.subject == 'bear'
    assert y.verb == 'eat'
    assert y.object == 'honey'

    z = parse_sentence(peekList2)
    assert z.subject == 'I'
    assert z.verb == 'want'
    assert z.object == 'drink some water'

def test_peek():
    """
    Testing the peek function
    """
    test = peek(peekList)
    assert test == "noun"

def test_match():
    """
    Testing the match function that takes a word_list and and expecting
    """
    testList = peekList.copy()
    test = match(testList, 'noun')
    assert test == ('noun','bear')
    test2 = match(testList, 'noun')
    assert test2 == None
    test3 = match(testList, 'stop')
    assert test3 == ('stop', 'the')

def test_skip():
    """
    Testing out the scenarios of skips
    """
    # Checking if it clears up all the stop words in the peekList
    testList = peekList.copy()
    # a = skip(testList, 'stop')
    checkList = peekList.copy()
    checkList.remove(('stop', 'the'))

    for i in range(0, len(testList)):
        a = skip(testList, 'stop')
        print(a)

def test_parse_verb():
    """
    Tetsing out the simple case to find the first verb
    """
    # Scenario 1 with stop word
    testList = peekList.copy()
    testVerb = parse_verb([
                        ('stop', 'To'),
                        ('verb', 'eat'),
                        ('noun', 'shit')
                        ])
    # Scenario 2 without stop word
    testVerb2 = parse_verb([
                        ('verb', 'fuck'),
                        ('noun', 'you')
                        ])
    assert testVerb == ('verb', 'eat')
    assert testVerb2 == ('verb', 'fuck')

    # Scenario 3 with error
    with pytest.raises(ParseError) as excinfo:
        parse_verb([
                ('stop', 'To'),
                ('noun', 'me')
                ])
        assert "Expected a verb next." in str(excinfo.value)

def test_parse_subject():
    """
    Three cases:
    1. first real word is a noun
    2. first real word is a Verb
    3. other
    """
    # Scenario 1
    testSubject = parse_subject([
                            ('stop', 'this'),
                            ('noun', 'man'),
                            ('verb', 'is'),
                            ('stop', 'a'),
                            ('noun', 'firefighter')
                                ])
    assert testSubject == ('noun', 'man')

    # Scenario 2
    testSubject2 = parse_subject([
                            ('verb', 'fuck'),
                            ('noun', 'you')
                                ])
    assert testSubject2 == ('noun', 'player')

    # Scenario 3
    with pytest.raises(ParseError) as excinfo:
        parse_subject([
                        ('stop', 'This'),
                        ('adjectives', 'wrong'),
                        ('noun', 'sentence')
                             ])
        assert "Expected a verb next." in str(excinfo.value)

def test_parse_object():
    """
    1. next word is a noun
    2. next word is a direction
    """
    # Scenario 1
    testObject = parse_object([
                            ('stop', 'To'),
                            ('direction', "North")
                            ])
    assert testObject == ('direction', 'North')

    # Scenario 2
    testObject2 = parse_object([
                            ('stop', 'To'),
                            ('noun', "Heaven")
                            ])
    assert testObject2 == ('noun', 'Heaven')

    # Scenario 3
    with pytest.raises(ParseError) as excinfo:
        parse_object([
                    ('verb', 'screw'),
                    ('noun', 'Busque'),
                    ('noun', 'Apple'),
                    ('verb', 'eat'),
                    ('stop', 'to')
                    ])
        assert "Expected a noun or dirtection next." in str(excinfo.value)
