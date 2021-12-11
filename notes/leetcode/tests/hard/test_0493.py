"""Test for Leetcode #493 - Reverse Pairs (Leetcode)"""
import sys
import pathlib

try:
    code_folder = "solutions/0493_reverse_pairs"
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
        "from solutions/0493_reverse_pairs, "
        "are you sure the solution exists?"
    )


def test_reverse_pairs():
    """simple test case for #493: `Reverse Pairs (Leetcode)`"""
    positional_inputs = []
    named_inputs = {}
    solver = Solution(*positional_inputs, **named_inputs)
    result = solver.solve()
    raise NotImplementedError("This test has not yet been implemented!")
