"""
    Construct Binary Search Tree from Preorder Traversal

    Q. Return the root node of a binary search tree that matches the given preorder traversal.

        (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a
        value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder
        traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

        It's guaranteed that for the given test cases there is always possible to find a binary search tree with the
        given requirements.

        Example 1:

        Input: [8,5,1,7,10,12]
        Output: [8,5,10,1,7,null,12]

        Constraints:

        1 <= preorder.length <= 100
        1 <= preorder[i] <= 10^8
        The values of preorder are distinct.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insert(self, node, val):
        if node is None:
            return TreeNode(val)
        if val < node.val:
            node.left = self.insert(node.left, val)
        else:
            node.right = self.insert(node.right, val)

        return node

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = None
        for each in preorder:
            root = self.insert(root, each)
        return root
