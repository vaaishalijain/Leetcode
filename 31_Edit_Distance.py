"""
    Edit Distance

    Q. Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

        You have the following 3 operations permitted on a word:

        Insert a character
        Delete a character
        Replace a character

        Example 1:

        Input: word1 = "horse", word2 = "ros"
        Output: 3
        Explanation:
        horse -> rorse (replace 'h' with 'r')
        rorse -> rose (remove 'r')
        rose -> ros (remove 'e')

        Example 2:

        Input: word1 = "intention", word2 = "execution"
        Output: 5
        Explanation:
        intention -> inention (remove 't')
        inention -> enention (replace 'i' with 'e')
        enention -> exention (replace 'n' with 'x')
        exention -> exection (replace 'n' with 'c')
        exection -> execution (insert 'u')

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @functools.lru_cache(None)
        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                return 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))

        return dfs(0, 0)
