import pytest
from ex49.ex48_convert import convert_number

def test_convert_number():
    assert type(convert_number(4)) == int
    assert convert_number("Spencer") == None
