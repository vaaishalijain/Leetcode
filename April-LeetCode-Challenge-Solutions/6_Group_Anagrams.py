"""
    Group Anagrams

    Q. Given an array of strings, group anagrams together.

        Example:

        Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
        Output:
        [
          ["ate","eat","tea"],
          ["nat","tan"],
          ["bat"]
        ]

        Note:

        All inputs will be in lowercase.
        The order of your output does not matter.

"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash, k = {}, 0
        ans = [[] for _ in range(len(strs))]
        for each in strs:
            temp_each = sorted(each)
            new_each = "".join(temp_each)
            if not hash.get(new_each) and hash.get(new_each)!=0:
                hash[new_each]=k
                k+=1
            index = hash.get(new_each)
            # print(hash, new_each, index)
            ans[index].append(each)
        final_ans = [x for x in ans if x != []]
        return final_ans