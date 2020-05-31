"""
    Ransom Note

    Q. Given an arbitrary ransom note string and another string containing letters from all the magazines, write a
       function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will
       return false.

        Each letter in the magazine string can only be used once in your ransom note.

        Note:
        You may assume that both strings contain only lowercase letters.

        canConstruct("a", "b") -> false
        canConstruct("aa", "ab") -> false
        canConstruct("aa", "aab") -> true

"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        temp = magazine
        for note in ransomNote:
            if note in temp:
                temp = temp.replace(note, '', 1)
            else:
                return False
        return True
