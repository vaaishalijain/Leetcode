"""
    Valid Palindrome

    Q. Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

        Note: For the purpose of this problem, we define empty string as valid palindrome.

        Example 1:

        Input: "A man, a plan, a canal: Panama"
        Output: true

        Example 2:

        Input: "race a car"
        Output: false

        Constraints:

        s consists only of printable ASCII characters.

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        i,j=0,n-1
        while i<j:
            # print(s[i],s[j], type(s[i]), type(s[j]))
            if not s[i].isalpha() and not s[i].isdigit():
                i+=1
            elif not s[j].isalpha() and not s[j].isdigit():
                j-=1
            elif s[i].lower() == s[j].lower():
                i+=1
                j-=1
            else:
                return False
        # print(i,j)
        return True