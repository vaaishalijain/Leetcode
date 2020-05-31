"""
    Maximal Square

    Q. Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return
       its area.

        Example:

        Input:

        1 0 1 0 0
        1 0 1 1 1
        1 1 1 1 1
        1 0 0 1 0

        Output: 4

"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n + 1)] for __ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return max([max(row) for row in dp]) ** 2
