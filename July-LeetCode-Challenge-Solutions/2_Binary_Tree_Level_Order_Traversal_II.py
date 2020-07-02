"""
    Binary Tree Level Order Traversal II

    Q. Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right,
       level by level from leaf to root).

        For example:
        Given binary tree [3,9,20,null,null,15,7],
            3
           / \
          9  20
            /  \
           15   7
        return its bottom-up level order traversal as:
        [
          [15,7],
          [9,20],
          [3]
        ]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        queue = []
        queue.append(root)
        ans = []
        while queue:
            temp = []
            for i in range(len(queue)):
                x = queue.pop(0)
                temp.append(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            ans.append(temp)
        return ans[::-1]
