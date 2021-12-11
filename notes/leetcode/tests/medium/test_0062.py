"""Test for Leetcode #62 - Grid Unique Paths"""
import sys
import pathlib

try:
    code_folder = "solutions/0062_unique_paths"
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
        "from solutions/0062_unique_paths, "
        "are you sure the solution exists?"
    )


def test_unique_paths():
    """simple test case for #62: `Grid Unique Paths`"""
    positional_inputs = []
    named_inputs = {}
    solver = Solution(*positional_inputs, **named_inputs)
    result = solver.solve()
    raise NotImplementedError("This test has not yet been implemented!")
