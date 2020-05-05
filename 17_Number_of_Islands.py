"""
    Number of Islands

    Q. Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by
       water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of
       the grid are all surrounded by water.

        Example 1:

        Input:
        11110
        11010
        11000
        00000

        Output: 1
        Example 2:

        Input:
        11000
        11000
        00100
        00011

        Output: 3

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) < 1:
            return 0
        m, n = len(grid), len(grid[0])
        cnt = 0

        def bfs_helper(r, c):
            if r < 0 or c < 0 or r > m - 1 or c > n - 1 or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            bfs_helper(r - 1, c)
            bfs_helper(r + 1, c)
            bfs_helper(r, c - 1)
            bfs_helper(r, c + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    bfs_helper(i, j)
        return cnt