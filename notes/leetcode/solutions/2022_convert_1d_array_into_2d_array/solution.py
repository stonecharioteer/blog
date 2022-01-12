"""Solution to Leetcode 2022 - 2022

Link : https://leetcode.com/problems/convert-1d-array-into-2d-array/
Level: easy
"""


class Solution:
    def __init__(self, *args, **kwargs):
        """Instantiates the solution object"""
        self.args = args
        self.kwargs = kwargs

    def solve(self, *args, **kwargs):
        """This implements the main solution"""
        raise NotImplementedError("This solution is not yet implemented.")

    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        array = []
        # check if the rearrangement is possible.
        if (m * n) != len(original):
            return array
        row = []
        for ix, item in enumerate(original):
            row.append(item)
            if (ix + 1) % n == 0:
                array.append(row)
                row = []

        return array
