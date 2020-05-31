"""
    Minimum Path Sum

    Q. Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
       the sum of all numbers along its path.

        Note: You can only move either down or right at any point in time.

        Example:

        Input:
        [
          [1,3,1],
          [1,5,1],
          [4,2,1]
        ]
        Output: 7
        Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m,n=len(grid), len(grid[0])
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i+1 <= m-1 and j+1 <= n-1:
                    grid[i][j]+= min(grid[i+1][j], grid[i][j+1])
                elif i+1 <= m-1:
                    grid[i][j]+=grid[i+1][j]
                elif j+1 <= n-1:
                    grid[i][j]+=grid[i][j+1]
        return grid[0][0]