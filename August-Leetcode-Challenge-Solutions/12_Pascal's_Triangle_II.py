"""
    Pascal's Triangle II

    Q. Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

        Note that the row index starts from 0.

        In Pascal's triangle, each number is the sum of the two numbers directly above it.

        Example:

        Input: 3
        Output: [1,3,3,1]
        Follow up:

        Could you optimize your algorithm to use only O(k) extra space?

"""


class Solution:
    def getRow(self, k: int) -> List[int]:
        i=0
        prev=[1]
        if k==0:
            return prev
        for i in range(k+1):
            row=[0]*(i+1)
            row[0]=row[-1]=1
            for j in range(1,i):
                row[j]=prev[j-1]+prev[j]
            prev=row
        return row