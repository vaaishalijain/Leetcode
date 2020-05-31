"""
    Contiguous Array

    Q. Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

        Example 1:
        Input: [0,1]
        Output: 2
        Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

        Example 2:
        Input: [0,1,0]
        Output: 2
        Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

        Note: The length of the given binary array will not exceed 50,000.

"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash = {}
        hash[0] = -1
        maxlen, cnt = 0, 0
        for i in range(len(nums)):
            cnt += 1 if nums[i] == 1 else -1
            if hash.get(cnt) is not None:
                maxlen = max(maxlen, i - hash.get(cnt))
            else:
                hash[cnt] = i
        return maxlen
