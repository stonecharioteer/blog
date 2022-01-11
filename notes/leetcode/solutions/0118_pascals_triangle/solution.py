"""Solution to Leetcode 118 - 118

Link : https://leetcode.com/problems/pascals-triangle/
Level: easy
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for index in range(1, numRows + 1):
            if index == 1:
                result.append([1])
            elif index == 2:
                result.append([1, 1])
            else:
                current_row = [0 for _ in range(index)]
                current_row[0] = current_row[-1] = 1
                for j in range(1, index - 1):
                    previous_row = result[-1]
                    current_row[j] = previous_row[j - 1] + previous_row[j]

                result.append(current_row)

        return result
