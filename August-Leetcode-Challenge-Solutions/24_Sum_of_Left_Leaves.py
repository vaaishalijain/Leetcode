"""
    Sum of Left Leaves

    Q. Find the sum of all left leaves in a given binary tree.

        Example:

            3
           / \
          9  20
            /  \
           15   7

        There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(root, isleft):
            if not root:
                return
            if isleft and not root.left and not root.right:
                self.ans += root.val
            helper(root.left, True)
            helper(root.right, False)

        self.ans = 0
        helper(root, False)
        return self.ans