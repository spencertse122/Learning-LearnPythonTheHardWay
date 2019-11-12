import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a __init__ that takes self and *** params.",

}
