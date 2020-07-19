"""
    Add Binary

    Q. Given two binary strings, return their sum (also a binary string).

        The input strings are both non-empty and contains only characters 1 or 0.

        Example 1:

        Input: a = "11", b = "1"
        Output: "100"

        Example 2:

        Input: a = "1010", b = "1011"
        Output: "10101"


        Constraints:

        Each string consists only of '0' or '1' characters.
        1 <= a.length, b.length <= 10^4
        Each string is either "0" or doesn't contain any leading zero.

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        i, j, c = 0, 0, 0
        ans = ''
        m, n = len(a), len(b)
        if m < n:
            a += '0' * (n - m)
        else:
            b += '0' * (m - n)
        while i < len(a):
            s = int(a[i]) + int(b[i]) + c
            if s == 2:
                c = 1
                ans += '0'
            elif s == 3:
                c = 1
                ans += '1'
            else:
                c = 0
                ans += str(s)
            i += 1
        if c > 0:
            ans += str(c)
        return ans[::-1]
