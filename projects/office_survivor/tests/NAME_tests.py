from nose.tools import *
import office_survivor

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!", end='')
