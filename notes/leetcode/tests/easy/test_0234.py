"""Test for Leetcode #234 - Check if a LinkedList is palindrome or not"""
import sys
import pathlib

try:
    code_folder = "solutions/0234_palindrome_linked_list"
    # the path here should be relative to the folder containing this folder and
    # the folder it points to should contain
    # a file named `solution.py` containing
    # a class named `Solution`
    # which has a method named `solve`
    absolute_code_path = pathlib.Path(code_folder).resolve().absolute()
    sys.path.append(code_folder)
    from solution import Solution
except ImportError:
    raise ImportError(
        "Unable to import solution.py "
        "from solutions/0234_palindrome_linked_list, "
        "are you sure the solution exists?"
    )


def test_palindrome_linked_list():
    """simple test case for #234: `Check if a LinkedList is palindrome or not`"""
    positional_inputs = []
    named_inputs = {}
    solver = Solution(*positional_inputs, **named_inputs)
    result = solver.solve()
    raise NotImplementedError("This test has not yet been implemented!")
