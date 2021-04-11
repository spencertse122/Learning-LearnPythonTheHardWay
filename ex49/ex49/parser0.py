"""
GOAL: produce a sentence object that has three attributes:
Subject, Verb, Object
"""
from ex49.lexicon import *

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

class SentenceParser(object):
    """
    An all in one parser to do all the parse functions, that takes in a regular sentence input
    and convert into list of tuples. And then use the sentence object as a validation.
    Added number support
    Added lower,upper cases
    """

    def __init__(self, SentenceToken):
        self.SentenceToken = scan(SentenceToken)

    def parse_sentence(self):
        subj = self.parse_subject()
        verb = self.parse_verb()
        obj = self.parse_object()
        return Sentence(subj, verb, obj)

    def parse_verb(self):
        """
        A way to loop through the list of scanned words
        """
        skip(self.SentenceToken, 'stop')

        if peek(self.SentenceToken) == 'verb':
            return match(self.SentenceToken, 'verb')
        else:
            raise ParseError("Expected a verb next.")

    def parse_object(self):
        skip(self.SentenceToken, 'stop')
        next_word = peek(self.SentenceToken)
        if next_word == 'noun':
            return match(self.SentenceToken, 'noun')
        elif next_word == 'direction':
            return match(self.SentenceToken, 'direction')
        else:
            raise ParseError("Expected a noun or direction next.")

    def parse_subject(self):
        skip(self.SentenceToken, 'stop')
        next_word = peek(self.SentenceToken)

        if next_word == 'noun':
            return match(self.SentenceToken, 'noun')
        elif next_word == 'verb':
            return ('noun', 'player')
        else:
            raise ParseError("Expected a verb next.")


def peek(word_list):
    """
    A way to peek at a potential tuple so we can make some decisons

    self.SentenceToken should be list of token tuples.
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

        if str(word[0]).lower() == expecting.lower():
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
    while (str(peek(word_list)).lower() == word_type) | (str(peek(word_list)).lower() == "number"):
        match(word_list, word_type)

        # Once it finds it it will just break
