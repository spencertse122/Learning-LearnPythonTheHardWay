# Defining Game Lexicon
game_lexicon = {
              'direction' : ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
              'verb' : ['go', 'stop', 'kill', 'eat'],
              'stop' : ['the', 'in', 'of', 'from', 'at', 'it'],
              'numbers' : [i for i in range(0, 10)]
              }

def getTag(word, LexiconDict):
    """
    A Function to parse a dictionary of list-of-tokens for scanning.
    Return a tuple of (tag, token)
    """
    tokenizedWord = None

    for key, value in LexiconDict.items():
        # First to see if it's a number
        try:
            int(word)
            tokenizedWord = ('number', int(word))
        except ValueError:
            # If it's not a number, try to see if it's within our lexicon
            try:
                if word.lower() in LexiconDict.get(key):
                    tokenizedWord = (key, word)
                    break
                # if it's all uppercase, we can assume it's an error as well
                elif word.upper() == word:
                    tokenizedWord = ('error', word)
                    break
                # if not, it will be a noun, some object
                else:
                    tokenizedWord = ('noun', word)
            # if some unknown variable type is parsed
            except AttributeError:
                tokenizedWord = ('error', word)
        except TypeError:
            tokenizedWord = ('error', word)
    return tokenizedWord


def scan(AString):
    """
    The scan function will take a string and tokenize it into
    list of string, and do the scanning based on the game_lexicon
    and return a list of tuples in format of (tag, token)
    """
    listOfStrings = AString.split()

    listOfTags = []
    for i in listOfStrings:
        tokenTag = getTag(i, game_lexicon)
        listOfTags.append(tokenTag)

    return listOfTags
