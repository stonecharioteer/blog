"""Solution to Leetcode 238 - 238

Link : https://leetcode.com/problems/product-of-array-except-self/
Level: medium
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

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first construct 2 arrays,
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
            right[-i - 1] = right[-i] * nums[-i]
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = left[i] * right[i]
        return result
