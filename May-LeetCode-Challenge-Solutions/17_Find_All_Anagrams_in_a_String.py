"""
    Find All Anagrams in a String

    Q. Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

        Strings consists of lowercase English letters only and the length of both strings s and p will not be larger
        than 20,100.

        The order of output does not matter.

        Example 1:

        Input:
        s: "cbaebabacd" p: "abc"

        Output:
        [0, 6]

        Explanation:
        The substring with start index = 0 is "cba", which is an anagram of "abc".
        The substring with start index = 6 is "bac", which is an anagram of "abc".

        Example 2:

        Input:
        s: "abab" p: "ab"

        Output:
        [0, 1, 2]

        Explanation:
        The substring with start index = 0 is "ab", which is an anagram of "ab".
        The substring with start index = 1 is "ba", which is an anagram of "ab".
        The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        p = Counter(p)
        ans, t = [], None
        for i in range(n - m + 1):
            if i == 0:
                t = Counter(s[:m])
            else:
                t[s[i - 1]] -= 1
                t[s[i + m - 1]] += 1
            if len(t - p) == 0:
                ans.append(i)
        return ans
