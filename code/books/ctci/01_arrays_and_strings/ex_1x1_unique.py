"""1.1 Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?"""


def is_unique(input_string):
    """determines if a string has all unique characters"""
    from collections import Counter

    counter = Counter(input_string)
    for char, values in counter.items():
        if values > 1:
            return False
    return True


def test_is_unique():
    assert is_unique("asdfg") == True
    assert is_unique("asssdffasdf") == False


def is_unique_without_counter(input_string):
    """Check if a string has all unique characters *without* using additional
    data structures"""
    input_string = sorted(input_string)
    last_char = None
    for char in input_string:
        if char == last_char:
            return False
        last_char = char
    return True


def test_is_unique_without_counter():
    assert is_unique_without_counter("asdfg") == True
    assert is_unique_without_counter("asssdffasdf") == False
