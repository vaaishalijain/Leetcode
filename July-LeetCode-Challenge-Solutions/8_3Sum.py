"""
    3Sum

    Q. Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique
       triplets in the array which gives the sum of zero.

        Note:

        The solution set must not contain duplicate triplets.

        Example:

        Given array nums = [-1, 0, 1, 2, -1, -4],

        A solution set is:
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        if not nums or nums[0] > 0 or nums[len(nums) - 1] < 0:
            return []
        for a in range(len(nums) - 2):
            if nums[a] > 0:
                break
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            i, j = a + 1, len(nums) - 1
            while i < j:
                val = nums[a] + nums[i] + nums[j]
                if val < 0:
                    i += 1
                elif val > 0:
                    j -= 1
                else:
                    ans.append([nums[a], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
        return ans
