"""
    Subsets

    Q. Given a set of distinct integers, nums, return all possible subsets (the power set).

        Note: The solution set must not contain duplicate subsets.

        Example:

        Input: nums = [1,2,3]
        Output:
        [
          [3],
          [1],
          [2],
          [1,2,3],
          [1,3],
          [2,3],
          [1,2],
          []
        ]

"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def helper(f, arr):
            # print(arr)
            if i == len(arr):
                ans.append(arr[:])
            for j in range(f, n):
                arr.append(nums[j])
                helper(j + 1, arr)
                arr.pop()

        for i in range(n + 1):
            helper(0, [])
        return ans
