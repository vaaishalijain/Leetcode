"""
    Longest Duplicate Substring

    Q. Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.
       (The occurrences may overlap.)

        Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated
        substring, the answer is "".)

        Example 1:

        Input: "banana"
        Output: "ana"
        Example 2:

        Input: "abcd"
        Output: ""


        Note:

        2 <= S.length <= 10^5
        S consists of lowercase English letters.
"""


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        n=len(S)
        arr=[ord(c)-ord('a') for c in S]
        start,end,pos=1,n,-1
        MOD = 2**63-1
        def search(m, MOD):
            h=0
            for i in range(m):
                h=(h*26+arr[i])%MOD
            s={h}
            ans=pow(26,m,MOD)
            for pos in range(1, n-m+1):
                h=(h*26-arr[pos-1]*ans+arr[pos+m-1])%MOD
                if h in s:
                    return pos
                s.add(h)
            return -1
        while start<=end:
            mid=int((start+end)/2)
            cur=search(mid,MOD)
            if cur!= -1:
                start=mid+1
                pos=cur
            else:
                end=mid-1
        return S[pos:pos+start-1]