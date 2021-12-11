"""Test for Leetcode #{{number}} - {{name}}"""
import sys
import pathlib
try:
    code_folder = "{{code_folder_path}}"
    # the path here should be relative to this folder
    # and the folder it points to should contain
    # a file named `solution.py` and another called `__init__.py`
    # and `solution.py` should contain a class named `Solution`
    # which has a method named `solve`
    absolute_code_path = pathlib.Path(code_folder).resolve().absolute()
    sys.path.append(code_folder)
    from solution import Solution
except ImportError:
    raise ImportError(
            "Unable to import solution.py "
            "from {{code_folder_path}}, ""are you sure the solution exists?")


def test_{{short_name}}():
    """simple test case for #{{number}}: `{{name}}`"""
    positional_inputs = []
    named_inputs = {}
    solver = Solution(*positional_inputs, **named_inputs)
    result = solver.solve()
    raise NotImplementedError("This test has not yet been implemented!")
