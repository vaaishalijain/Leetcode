"""
    Word Break II

    Q. Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to
       construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

        Note:

        The same word in the dictionary may be reused multiple times in the segmentation.
        You may assume the dictionary does not contain duplicate words.
        Example 1:

        Input:
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        Output:
        [
          "cats and dog",
          "cat sand dog"
        ]
        Example 2:

        Input:
        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
        Output:
        [
          "pine apple pen apple",
          "pineapple pen apple",
          "pine applepen apple"
        ]
        Explanation: Note that you are allowed to reuse a dictionary word.
        Example 3:

        Input:
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        Output:
        []
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wd = set()
        for w in wordDict:
            wd |= set(w)
        if not set(s).issubset(wd):
            return []

        def helper(i, temp):
            if i == n:
                ans.append(' '.join(temp))
            else:
                for k in d:
                    if s[i:i + k] in d[k]:
                        helper(i + k, temp + [s[i:i + k]])

        ans = []
        d = defaultdict(set)
        for w in wordDict:
            d[len(w)].add(w)
        helper(0, [])
        return ans
