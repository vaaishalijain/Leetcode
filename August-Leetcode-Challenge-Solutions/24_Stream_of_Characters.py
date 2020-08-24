"""
    Stream of Characters

    Q. Implement the StreamChecker class as follows:

        StreamChecker(words): Constructor, init the data structure with the given words.
        query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest
        to newest, including this letter just queried) spell one of the words in the given list.

        Example:

        StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
        streamChecker.query('a');          // return false
        streamChecker.query('b');          // return false
        streamChecker.query('c');          // return false
        streamChecker.query('d');          // return true, because 'cd' is in the wordlist
        streamChecker.query('e');          // return false
        streamChecker.query('f');          // return true, because 'f' is in the wordlist
        streamChecker.query('g');          // return false
        streamChecker.query('h');          // return false
        streamChecker.query('i');          // return false
        streamChecker.query('j');          // return false
        streamChecker.query('k');          // return false
        streamChecker.query('l');          // return true, because 'kl' is in the wordlist

        Note:

        1 <= words.length <= 2000
        1 <= words[i].length <= 2000
        Words will only consist of lowercase English letters.
        Queries will only consist of lowercase English letters.
        The number of queries is at most 40000.

"""


class StreamChecker:

    def insert(self, words):
        for word in words:
            node = self.trie
            word = word[::-1]
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node['end'] = 1

    def __init__(self, words: List[str]):
        self.trie = defaultdict(dict)
        self.insert(words)
        self.curr = ''
        # print(self.trie)

    def query(self, letter: str) -> bool:
        self.curr += letter
        node = self.trie
        for a in reversed(self.curr):
            if a not in node:
                break
            node = node[a]
            if 'end' in node:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)