# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0

        current = head
        while current is not None:
            current = current.next
            length += 1

        from math import floor
        middle = floor(length/2) + 1

        i = 1
        current = head
        while i < middle:
            i += 1
            current = current.next

        return current
