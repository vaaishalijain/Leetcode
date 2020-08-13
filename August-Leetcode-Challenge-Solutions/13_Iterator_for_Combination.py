"""
    Iterator for Combination

    Q. Design an Iterator class, which has:

        A constructor that takes a string characters of sorted distinct lowercase English letters and a number
        combinationLength as arguments.
        A function next() that returns the next combination of length combinationLength in lexicographical order.
        A function hasNext() that returns True if and only if there exists a next combination.

        Example:

        CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

        iterator.next(); // returns "ab"
        iterator.hasNext(); // returns true
        iterator.next(); // returns "ac"
        iterator.hasNext(); // returns true
        iterator.next(); // returns "bc"
        iterator.hasNext(); // returns false

        Constraints:

        1 <= combinationLength <= characters.length <= 15
        There will be at most 10^4 function calls per test.
        It's guaranteed that all calls of the function next are valid.

"""


class CombinationIterator:

    def generate(self, s, n, t, st):
        if len(t) == n:
            self.ans.append(''.join(t))
        for i in range(st, len(s)):
            t.append(s[i])
            self.generate(s, n, t, i + 1)
            t.pop()

    def __init__(self, s: str, n: int):
        self.ans, self.it = [], 0
        comb = self.generate(s, n, [], 0)
        # print(self.ans)

    def next(self) -> str:
        if self.it < len(self.ans):
            val = self.ans[self.it]
            self.it += 1
            return val

    def hasNext(self) -> bool:
        if self.ans and self.it < len(self.ans):
            return True
        return False

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()