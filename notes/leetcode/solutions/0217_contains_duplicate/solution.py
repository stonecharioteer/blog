"""Solution to Leetcode 217 - 217

Link : https://leetcode.com/problems/contains-duplicate/
Level: easy
"""
from typing import List


class Solution:
    def __init__(self, *args, **kwargs):
        """Instantiates the solution object"""
        self.args = args
        self.kwargs = kwargs

    def containsDuplicate(self, nums: List[int]) -> bool:
        items = {}
        for item in nums:
            if items.get(item) is not None:
                return True
            else:
                items[item] = 1
        return False

    def solve(self, *args, **kwargs):
        """This implements the main solution"""
        return self.containsDuplicate(args[0])
