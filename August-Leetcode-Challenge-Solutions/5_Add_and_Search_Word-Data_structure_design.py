"""
    Add and Search Word - Data structure design

    Q. Design a data structure that supports the following two operations:

        void addWord(word)
        bool search(word)
        search(word) can search a literal word or a regular expression string containing only letters a-z or .. A .
        means it can represent any one letter.

        Example:

        addWord("bad")
        addWord("dad")
        addWord("mad")
        search("pad") -> false
        search("bad") -> true
        search(".ad") -> true
        search("b..") -> true
        Note:
        You may assume that all words are consist of lowercase letters a-z.

"""


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = collections.defaultdict(list)
        self.trieset = set()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie[len(word)].append(word)
        self.trieset.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if word in self.trieset:
            return True
        node = self.trie
        for k in node[len(word)]:
            for i, j in enumerate(word):
                if j != k[i] and j != '.':
                    break
            else:
                return True
        return False

    # Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)