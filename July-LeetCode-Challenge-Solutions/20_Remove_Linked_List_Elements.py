"""
    Remove Linked List Elements

    Q. Remove all elements from a linked list of integers that have value val.

        Example:

        Input:  1->2->6->3->4->5->6, val = 6
        Output: 1->2->3->4->5

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        d = ListNode(0)
        d.next = head
        t1, t = d, head
        while t is not None:
            if t.val == val:
                t1.next = t.next
            else:
                t1 = t
            t = t.next
        return d.next
