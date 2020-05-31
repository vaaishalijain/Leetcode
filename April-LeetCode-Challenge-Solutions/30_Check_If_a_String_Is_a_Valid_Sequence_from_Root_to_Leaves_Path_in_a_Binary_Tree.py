"""
    Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree

    Q. Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given
       string is a valid sequence in such binary tree.

        Example 1:

        Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
        Output: true
        Explanation:
        The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
        Other valid sequences are:
        0 -> 1 -> 1 -> 0
        0 -> 0 -> 0

        Example 2:

        Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
        Output: false
        Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.

        Example 3:

        Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
        Output: false
        Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def validHelper(root, i):
            if root and root.left is None and root.right is None and i == len(arr) - 1 and root.val == arr[i]:
                return True
            if root and i < len(arr) and root.val == arr[i]:
                l = validHelper(root.left, i + 1)
                r = validHelper(root.right, i + 1)
                return l or r
            return False

        return validHelper(root, 0)
