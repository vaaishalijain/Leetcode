"""
    Valid Parenthesis String

    Q. Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether
       this string is valid. We define the validity of a string by these rules:

        1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
        2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
        3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
        4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
        5. An empty string is also valid.

        Example 1:

        Input: "()"
        Output: True

        Example 2:

        Input: "(*)"
        Output: True

        Example 3:

        Input: "(*))"
        Output: True

        Note:
        1. The string size will be in the range [1, 100].

"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        lb, rb =0,0
        for i in range(len(s)):
            if s[i] in "(*":
                lb+=1
            else:
                lb-=1
            if s[len(s)-i-1] in "*)":
                rb+=1
            else:
                rb-=1
            if lb < 0 or rb < 0:
                return False
        return True