"""Solution to Leetcode 287 - 287

Link : https://leetcode.com/problems/find-the-duplicate-number/
Level: medium
"""


class Solution:
    def __init__(self, *args, **kwargs):
        """Instantiates the solution object"""
        self.args = args
        self.kwargs = kwargs

    def solve(self, *args, **kwargs):
        """This implements the main solution"""
        raise NotImplementedError("This solution is not yet implemented.")

    def findDuplicate(self, nums: List[int]) -> int:
        from collections import defaultdict

        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
            if nums_dict[num] == 2:
                return num
        return -1
