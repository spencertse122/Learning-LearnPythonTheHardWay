# from nose.tools import *
# For some reason, nose test doesn't work, so we switch to pytest for the rest of the exercise

import pytest
import NAME

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!", end='')
