"""
    Ugly Number II

    Q. Write a program to find the n-th ugly number.

        Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

        Example:

        Input: n = 10
        Output: 12
        Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
        Note:

        1 is typically treated as an ugly number.
        n does not exceed 1690.

"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        a=[0]*n
        a[0]=1
        t1=t2=t3=0
        for i in range(1,n):
            a[i]=min(a[t1]*2,a[t2]*3,a[t3]*5)
            if a[i]==a[t1]*2:
                t1+=1
            if a[i]==a[t2]*3:
                t2+=1
            if a[i]==a[t3]*5:
                t3+=1
        return a[n-1]