"""
    Find All Duplicates in an Array

    Q. Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

        Find all the elements that appear twice in this array.

        Could you do it without extra space and in O(n) runtime?

        Example:
        Input:
        [4,3,2,7,8,2,3,1]

        Output:
        [2,3]

"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        ans=[]
        for i in nums:
            if nums[abs(i)-1]<0:
                ans.append(abs(i))
            else:
                nums[abs(i)-1]=nums[abs(i)-1] * -1
        return ans