"""
    Power of Four

    Q. Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

        Example 1:

        Input: 16
        Output: true

        Example 2:

        Input: 5
        Output: false
        Follow up: Could you solve it without loops/recursion?

"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if not num or num < 0:
            return False
        val = math.log(abs(num), 4)
        return math.ceil(val) == math.floor(val)
