"""
    Numbers With Same Consecutive Differences

    Q. Return all non-negative integers of length N such that the absolute difference between every two consecutive
       digits is K.

        Note that every number in the answer must not have leading zeros except for the number 0 itself. For example,
        01 has one leading zero and is invalid, but 0 is valid.

        You may return the answer in any order.

        Example 1:

        Input: N = 3, K = 7
        Output: [181,292,707,818,929]
        Explanation: Note that 070 is not a valid number, because it has leading zeroes.

        Example 2:

        Input: N = 2, K = 1
        Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


        Note:

        1 <= N <= 9
        0 <= K <= 9

"""


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:

        if N == 1:
            return range(10)

        @lru_cache(None)
        def helper(i, j):
            if j < 0 or j > 9 or (j == 0 and i == 1):
                return []
            if i == 1:
                return [str(j)]
            direction = set([K, -K])
            temp = []
            for l in direction:
                temp += [x + str(j) for x in helper(i - 1, j + l)]
            return temp

        ans = list(chain(*[helper(N, i) for i in range(10)]))
        return ans

        '''
        def helper(temp):
            if len(temp)==N:
                self.ans.append(int(temp))
                return
            for i in range(10):
                if temp:
                    last=temp[-1]
                    if abs(int(last)-i)==K:
                        helper(temp+str(i))
                elif i!=0 or N==1:
                    helper(temp+str(i))
        self.ans=[]
        helper('')
        return self.ans
        '''