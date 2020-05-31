"""
    Search in Rotated Sorted Array

    Q. Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

        (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

        You are given a target value to search. If found in the array return its index, otherwise return -1.

        You may assume no duplicate exists in the array.

        Your algorithm's runtime complexity must be in the order of O(log n).

        Example 1:

        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4
        Example 2:

        Input: nums = [4,5,6,7,0,1,2], target = 3
        Output: -1

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        n = len(nums)
        start = 0
        end = n - 1
        while start <= end:
            mid = (end - start) // 2 + start
            if nums[mid] == target:
                return mid
            if nums[mid] == nums[start]:
                if target == nums[end]:
                    return end
                return -1
            if nums[mid] > nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid
                else:
                    end = mid
        return -1
