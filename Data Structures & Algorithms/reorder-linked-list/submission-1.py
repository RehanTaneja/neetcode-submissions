# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return 
        if head.next.next is None:
            return
        if head.next.next.next is None:
            second = head.next
            last = head.next.next
            head.next = last
            last.next = second
            second.next = None
            return
        first = head
        last = first
        second_last = None
        while last.next is not None:
            second_last = last
            last = last.next
        second = first.next
        first.next = last
        second_last.next = None
        self.reorderList(second)
        last.next = second
        