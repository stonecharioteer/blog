"""Test for Leetcode #31 - Next Permutation"""
import sys
import pathlib

try:
    code_folder = "solutions/0031_next_permutation"
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
        "from solutions/0031_next_permutation, "
        "are you sure the solution exists?"
    )


def test_next_permutation():
    """simple test case for #31: `Next Permutation`"""
    positional_inputs = []
    named_inputs = {}
    solver = Solution(*positional_inputs, **named_inputs)
    result = solver.solve()
    raise NotImplementedError("This test has not yet been implemented!")
