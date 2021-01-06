# Create a secondary test to observe how pytest works.
import pytest
import NAME

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!", end='')
