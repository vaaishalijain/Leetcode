"""
    Coin Change 2

    Q. You are given coins of different denominations and a total amount of money. Write a function to compute the
       number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

        Example 1:

        Input: amount = 5, coins = [1, 2, 5]
        Output: 4
        Explanation: there are four ways to make up the amount:
        5=5
        5=2+2+1
        5=2+1+1+1
        5=1+1+1+1+1

        Example 2:

        Input: amount = 3, coins = [2]
        Output: 0
        Explanation: the amount of 3 cannot be made up just with coins of 2.

        Example 3:

        Input: amount = 10, coins = [10]
        Output: 1

        Note:

        You can assume that

        0 <= amount <= 5000
        1 <= coin <= 5000
        the number of coins is less than 500
        the answer is guaranteed to fit into signed 32-bit integer

"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        if n==0:
            return int(n==amount)
        dp=[[0]*n for _ in range(amount+1)]
        for i in range(n):
            dp[0][i]=1
        for i in range(amount):
            for j in range(n):
                dp[i+1][j]=dp[i+1][j-1]
                if i+1 - coins[j]>=0:
                    dp[i+1][j]+=dp[i+1-coins[j]][j]
        return dp[-1][-1]