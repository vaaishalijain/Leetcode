"""
    Cousins in Binary Tree

    Q. In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

        Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

        We are given the root of a binary tree with unique values, and the values x and y of two different nodes in
        the tree.

        Return true if and only if the nodes corresponding to the values x and y are cousins.

        Example 1:

        Input: root = [1,2,3,4], x = 4, y = 3
        Output: false

        Example 2:

        Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
        Output: true

        Example 3:

        Input: root = [1,2,3,null,4], x = 2, y = 3
        Output: false

        Note:

        The number of nodes in the tree will be between 2 and 100.
        Each node has a unique integer value from 1 to 100.

"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def check(root, l, a, par):
            if not root:
                return []
            if root.val==a:
                return [l, par.val]
            return check(root.left, l+1, a, root) + check(root.right, l+1, a, root)

        vx = check(root, 1, x, root)
        vy = check(root, 1, y, root)
        return vx[0]==vy[0] and vx[1]!=vy[1]
