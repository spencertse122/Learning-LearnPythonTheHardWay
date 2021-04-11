"""
GOAL: produce a sentence object that has three attributes:
Subject, Verb, Object
"""

class ParseError(Exception):
    pass

class Sentence(object):
    """
    A sentence object represent a regular sentense that has
    a subject, an object, and a verb.

    The sentence object takes tuples token instead of an actual word to create.
    """
    def __init__(self, subject, verb, obj):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1] # since it's a tuple, we have to index the second item (the actual word)
        self.verb = verb[1] # and then it's a string
        self.object = obj[1]

def peek(word_list):
    """
    A way to peek at a potential tuple so we can make some decisons

    word_list should be list of token tuples.
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
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    """
    a way to skip things we do not care about
    like stop words
    """
    # The peek will look at the first item
    # So if it's the word type is something we want to skip, we pop it
    # popping it with the atch function
    while peek(word_list) == word_type:
        match(word_list, word_type)

        # Once it finds it it will just break

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
    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParseError("Expected a noun or direction next.")

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParseError("Expected a verb next.")

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
