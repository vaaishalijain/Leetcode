"""
    Perfect Squares

    Q. Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...)
       which sum to n.

        Example 1:

        Input: n = 12
        Output: 3
        Explanation: 12 = 4 + 4 + 4.
        Example 2:

        Input: n = 13
        Output: 2
        Explanation: 13 = 4 + 9.

"""


class Solution:
    def numSquares(self, n: int) -> int:
        if sqrt(n).is_integer():
            return 1
        s1, s2 = [0], [n]
        ps = [i ** 2 for i in range(1, floor(sqrt(n)) + 1)]
        visited1, visited2 = set([0]), set([n])
        cnt1, cnt2 = 0, 0

        while len(s1) > 0 and len(s2) > 0:
            cnt1 += 1
            for _ in range(len(s1)):
                a = s1.pop(0)
                for b in ps:
                    x = a + b
                    if x in visited2:
                        return cnt1 + cnt2
                    if x not in visited1 and x < n:
                        visited1.add(x)
                        s1.append(x)
            cnt2 += 1
            for _ in range(len(s2)):
                a = s2.pop(0)
                for b in ps:
                    x = a - b
                    if x in visited1:
                        return cnt1 + cnt2
                    if x not in visited2 and x > 0:
                        visited2.add(x)
                        s2.append(x)
