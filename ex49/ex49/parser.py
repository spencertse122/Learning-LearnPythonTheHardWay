"""
GOAL: produce a sentence object that has three attributes:
Subject, Verb, Object
"""

class ParserError(Exception):
    pass

class Sentence(object):
    """
    A sentence object to put the results in
    """
    def __init__(self, subject, verb, obj):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

def peek(word_list):
    """
    A way to peek at a potential tuple so we can make some decisons
    """
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    """
    A way to match different types of tuples that we expect in
    our Subject Verb Object Setup.
    """
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return words
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    """
    a way to skip things we do not care about
    like stop words
    """
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    """
    A way to loop through the list of scanned words
    """
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParseError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)
    if next_word = 'noun':
        return match(word)list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")
