"""
    Single Element in a Sorted Array

    Q. You are given a sorted array consisting of only integers where every element appears exactly twice, except for
       one element which appears exactly once. Find this single element that appears only once.

        Example 1:

        Input: [1,1,2,3,3,4,4,8,8]
        Output: 2

        Example 2:

        Input: [3,3,7,7,10,11,11]
        Output: 10

        Note: Your solution should run in O(log n) time and O(1) space.

"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        s, e = 0, n - 1
        while s <= e:
            if nums[s] == nums[s + 1]:
                s += 2
            else:
                return nums[s]
            if nums[e] == nums[e - 1]:
                e -= 2
            else:
                return nums[e]
