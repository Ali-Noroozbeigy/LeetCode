# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        i = 1
        while(l1.next is not None and l2.next is not None):
            temp = l1 + l2
            carry = temp // (10 ** i)
            digit = temp % 10

            l1 = digit
            l2 = digit

            l1.next.val += carry

            l1 = l1.next
            l2 = l2.next

        if (l1.next is None and l2.next is None):
            temp = l1 + l2
            carry = temp // (10 ** i)
            digit = temp % 10

            l1 = digit
            l2 = digit

            l1.next = ListNode(val=carry)
            return 