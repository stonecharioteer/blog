"""Test for Leetcode #19 - Remove N-th node from back of LinkedList"""
import sys
import pathlib

try:
    code_folder = "solutions/0019_remove_nth_node_from_end_of_list"
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
        "from solutions/0019_remove_nth_node_from_end_of_list, "
        "are you sure the solution exists?"
    )


def test_remove_nth_node_from_end_of_list():
    """simple test case for #19: `Remove N-th node from back of LinkedList`"""
    positional_inputs = []
    named_inputs = {}
    solver = Solution(*positional_inputs, **named_inputs)
    result = solver.solve()
    raise NotImplementedError("This test has not yet been implemented!")
