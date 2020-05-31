"""
    Move Zeroes

    Q. Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
       the non-zero elements.

        Example:

        Input: [0,1,0,3,12]
        Output: [1,3,12,0,0]
        Note:

        You must do this in-place without making a copy of the array.
        Minimize the total number of operations.

"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        t1, t2 = 0, 0
        while t2 < len(nums):
            if nums[t1] == 0 and nums[t2] != 0:
                nums[t1], nums[t2] = nums[t2], nums[t1]
            if nums[t1] != 0:
                t1 += 1
            t2 += 1
