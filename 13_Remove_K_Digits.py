"""
    Remove K Digits

    Q. Given a non-negative integer num represented as a string, remove k digits from the number so that the new number
       is the smallest possible.

        Note:
        The length of num is less than 10002 and will be ≥ k.
        The given num does not contain any leading zero.
        Example 1:

        Input: num = "1432219", k = 3
        Output: "1219"
        Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
        Example 2:

        Input: num = "10200", k = 1
        Output: "200"
        Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
        Example 3:

        Input: num = "10", k = 2
        Output: "0"
        Explanation: Remove all the digits from the number and it is left with nothing which is 0.

"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num:
            return "0"
        i = 0
        while i < len(num)-1 and k >0:
            if num[i] > num[i+1]:
                num = num[:i] + num[i+1:]
                i = i-1 if i!=0 else 0
                k-=1
            else:
                i+=1
        return  num.lstrip("0")[:len(num)-k] or "0"