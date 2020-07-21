"""
    Word Search

    Q. Given a 2D board and a word, find if the word exists in the grid.

        The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
        horizontally or vertically neighboring. The same letter cell may not be used more than once.

        Example:

        board =
        [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]

        Given word = "ABCCED", return true.
        Given word = "SEE", return true.
        Given word = "ABCB", return false.


        Constraints:

        board and word consists only of lowercase and uppercase English letters.
        1 <= board.length <= 200
        1 <= board[i].length <= 200
        1 <= word.length <= 10^3

"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i, j, k):
            if self.flag:
                return
            if k == len(word):
                self.flag = True
                return
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            temp = board[i][j]
            if board[i][j] != word[k]:
                return
            board[i][j] = '#'
            k += 1
            helper(i + 1, j, k)
            helper(i, j + 1, k)
            helper(i - 1, j, k)
            helper(i, j - 1, k)
            board[i][j] = temp

        m, n = len(board), len(board[0])
        self.flag = False
        for i in range(m):
            for j in range(n):
                helper(i, j, 0)
        return self.flag