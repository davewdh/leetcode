# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            if l1:
                value1 = l1.val
            else:
                value1 = 0
            if l2:
                value2 = l2.val
            else:
                value2 = 0
            val = value1 + value2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
