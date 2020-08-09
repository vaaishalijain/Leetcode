"""
    Rotting Oranges

    Q. In a given grid, each cell can have one of three values:

        the value 0 representing an empty cell;
        the value 1 representing a fresh orange;
        the value 2 representing a rotten orange.
        Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

        Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

        Example 1:

        Input: [[2,1,1],[1,1,0],[0,1,1]]
        Output: 4

        Example 2:

        Input: [[2,1,1],[0,1,1],[1,0,1]]
        Output: -1
        Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

        Example 3:

        Input: [[0,2]]
        Output: 0
        Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

        Note:

        1 <= grid.length <= 10
        1 <= grid[0].length <= 10
        grid[i][j] is only 0, 1, or 2.

"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        queue = []
        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    total += 1
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        cnt = len(queue)
        if total == 0:
            return 0
        if cnt == 0:
            return -1
        k = 0
        while queue:
            i, j, k = queue.pop(0)
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                a, b = i + x, j + y
                if a >= 0 and a < m and b >= 0 and b < n:
                    if grid[a][b] == 1:
                        grid[a][b] = 2
                        queue.append((a, b, k + 1))
                        cnt += 1

        if cnt < total:
            return -1
        return k