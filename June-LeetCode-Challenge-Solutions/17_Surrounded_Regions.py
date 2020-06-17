"""
    Surrounded Regions

    Q. Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

        A region is captured by flipping all 'O's into 'X's in that surrounded region.

        Example:

        X X X X
        X O O X
        X X O X
        X O X X
        After running your function, the board should be:

        X X X X
        X X X X
        X X X X
        X O X X
        Explanation:

        Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to
        'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
        Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if not m:
            return
        n = len(board[0])

        def edgeCheck(board, a, b, orig, new):
            if a >= m or b >= n or a < 0 or b < 0:
                return
            if board[a][b] != orig:
                return
            board[a][b] = new
            edgeCheck(board, a + 1, b, orig, new)
            edgeCheck(board, a - 1, b, orig, new)
            edgeCheck(board, a, b + 1, orig, new)
            edgeCheck(board, a, b - 1, orig, new)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'L'

        for i in range(m):
            if board[i][0] == 'L':
                edgeCheck(board, i, 0, 'L', 'O')
        for i in range(m):
            if board[i][n - 1] == 'L':
                edgeCheck(board, i, n - 1, 'L', 'O')
        for i in range(n):
            if board[0][i] == 'L':
                edgeCheck(board, 0, i, 'L', 'O')
        for i in range(n):
            if board[m - 1][i] == 'L':
                edgeCheck(board, m - 1, i, 'L', 'O')

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'L':
                    board[i][j] = 'X'
