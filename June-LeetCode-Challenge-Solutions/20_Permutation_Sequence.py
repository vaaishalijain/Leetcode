"""
    Permutation Sequence

    Q. The set [1,2,3,...,n] contains a total of n! unique permutations.

        By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

        "123"
        "132"
        "213"
        "231"
        "312"
        "321"
        Given n and k, return the kth permutation sequence.

        Note:

        Given n will be between 1 and 9 inclusive.
        Given k will be between 1 and n! inclusive.

        Example 1:

        Input: n = 3, k = 3
        Output: "213"

        Example 2:

        Input: n = 4, k = 9
        Output: "2314"

"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact, dig = [1] * n, [1] * n
        for i in range(1, n):
            fact[i] = (i + 1) * fact[i - 1]
            dig[i] = i + 1
        ans = ''
        while len(ans) < n - 1:
            rep = fact[-2]
            ne = int((k - 1) / rep)
            ans += str(dig[ne])
            dig.pop(ne)
            fact.pop()
            k = k % rep
            if k == 0:
                for i in range(len(dig) - 1, -1, -1):
                    ans += str(dig[i])

        if len(ans) < n:
            ans += str(dig[0])
        return ans