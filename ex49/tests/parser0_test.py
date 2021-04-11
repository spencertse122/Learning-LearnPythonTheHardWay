import pytest
from ex49.parser0 import *

GoodSentence = "The bears go to North and eat an apple."
GoodSentence2 = "We kill 5 bear in the North"
BadSentence = " north people in go 9"


def test_parse_goodsentence():
    """
    Testing the good scenario
    """
    # Good Scenario
    testSentence = SentenceParser(GoodSentence)
    structuredSentence = testSentence.parse_sentence()

    assert structuredSentence.subject == "bears"
    assert structuredSentence.verb == "go"
    assert structuredSentence.object == "North"

def test_parse_badsentence():
    """
    Testing the bad scenario
    """
    testBad = SentenceParser(BadSentence)
    with pytest.raises(ParseError) as excinfo:
        structuredSentence = testBad.parse_sentence()
        assert structuredSentence.subject == "north"
        assert "Expected a verb next." in str(excinfo.value)

def test_parse_numsentence():
    """
    Testing the number Scenario
    """
    testSentence = SentenceParser(GoodSentence2)
    structuredSentence = testSentence.parse_sentence()

    assert structuredSentence.subject == "We"
    assert structuredSentence.verb == "kill"
    assert structuredSentence.object == "bear"
