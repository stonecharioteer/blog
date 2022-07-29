"""Solution to Leetcode 136 - 136

Link : https://leetcode.com/problems/single-number/
Level: easy
"""
from typing import List


class Solution:
    def __init__(self, *args, **kwargs):
        """Instantiates the solution object"""
        self.args = args
        self.kwargs = kwargs

    def solve(self, *args, **kwargs):
        """This implements the main solution"""
        raise NotImplementedError("This solution is not yet implemented.")

    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result
