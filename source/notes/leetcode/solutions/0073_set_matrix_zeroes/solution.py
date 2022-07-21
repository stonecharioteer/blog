"""Solution to Leetcode 73 - 73

Link : https://leetcode.com/problems/set-matrix-zeroes/
Level: medium
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # first note down where the zeroes are.
        zeroes = []
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == 0:
                    zeroes.append((i, j))
        for (i, j) in zeroes:
            # item at i x j is 0,
            # set row i to zero
            # set col j to zero
            matrix[i] = [0 for _ in matrix[i]]
            for row, _ in enumerate(matrix):
                matrix[row][j] = 0
