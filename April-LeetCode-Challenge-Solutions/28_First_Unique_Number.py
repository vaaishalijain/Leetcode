"""
    First Unique Number

    Q. You have a queue of integers, you need to retrieve the first unique integer in the queue.

        Implement the FirstUnique class:
            - FirstUnique(int[] nums) Initializes the object with the number in the queue.
            - int FirstUnique() returns the value of the first unique integer of the queue, and return -1 if there is
              no such integer.
            - void add(int value) insert value to the queue.

        Example 1:

        Input:
        ["FirstUnique", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique"]
        [[[2,3,5]], [], [5], [], [2], [], [3], []]

        Output:
        [null,2,null,2,null,3,null,-1]

        Explanation:
        FirstUnique firstUnique = new FirstUnique([2,3,5]);
        firstUnique.showFirstUnique();  // return 2
        firstUnique.add(5);             // the queue is now [2,3,5,5]
        firstUnique.showFirstUnique();  // return 2
        firstUnique.add(2);             // the queue is now [2,3,5,5,2]
        firstUnique.showFirstUnique();  // return 3
        firstUnique.add(3);             // the queue is now [2,3,5,5,2,3]
        firstUnique.showFirstUnique();  // return -1

"""

from collections import OrderedDict


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.hash = OrderedDict()
        self.lastFound = -1
        for i, j in enumerate(nums):
            self.add(j)
        # print(list(self.hash))

    def showFirstUnique(self) -> int:
        # print(self.hash)
        return self.lastFound if self.hash[self.lastFound] <= 1 else -1
        # return self.lastFound

    def add(self, value: int) -> None:

        if value not in self.hash:
            self.hash[value] = 1
            if self.lastFound == -1 or self.hash[self.lastFound] > 1:
                self.lastFound = value
        else:
            self.hash[value] += 1
            self.hash.move_to_end(value)
            # print(self.lastFound, self.hash, self.hash.get(self.lastFound))
            if self.hash[self.lastFound] > 1:
                for i, j in self.hash.items():
                    self.lastFound = i
                    break

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)