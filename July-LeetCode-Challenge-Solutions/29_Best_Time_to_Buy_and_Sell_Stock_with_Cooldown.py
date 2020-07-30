"""
    Best Time to Buy and Sell Stock with Cooldown

    Q. Say you have an array for which the ith element is the price of a given stock on day i.

        Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one
        and sell one share of the stock multiple times) with the following restrictions:

        You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
        After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
        Example:

        Input: [1,2,3,0,2]
        Output: 3
        Explanation: transactions = [buy, sell, cooldown, buy, sell]

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n<2:
            return 0
        pr=[0]*(n-1)
        dp=[0]*(n+1)
        dpm =[0]*(n+1)
        for i in range(n-1):
            pr[i]=prices[i+1]-prices[i]
        for i in range(n-1):
            dp[i]=pr[i]+max(dp[i-1],dpm[i-3])
            dpm[i]=max(dp[i],dpm[i-1])
        # print(dpm)
        return dpm[-3]