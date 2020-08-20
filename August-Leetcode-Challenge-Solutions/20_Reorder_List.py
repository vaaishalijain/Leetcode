"""
    Reorder List

    Q. Given a singly linked list L: L0→L1→…→Ln-1→Ln, reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

        You may not modify the values in the list's nodes, only nodes itself may be changed.

        Example 1:

        Given 1->2->3->4, reorder it to 1->4->2->3.

        Example 2:

        Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        s=head
        f=head
        while f.next and f.next.next:
            s=s.next
            f=f.next.next
        p=None
        c=s.next
        while c:
            n=c.next
            c.next=p
            p=c
            c=n
        s.next=None
        h1,h2=head,p
        while h2:
            n=h1.next
            h1.next=h2
            h1=h2
            h2=n