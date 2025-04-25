# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev = dummy
        cur = head
        #   1, 2 -> 3, 4 ,5. 2 -> t = 3, 2 -> d(None), d = 2, <- cur = 3, 3 -> 2
        #   p, c   t.  d
        for i in range(left - 1): 
            leftPrev = cur
            cur = cur.next

        dummy2 = None
        for i in range(right - left + 1):
            temp = cur.next
            cur.next = dummy2
            dummy2 = cur
            cur = temp

        leftPrev.next.next = cur
        leftPrev.next = dummy2

        return dummy.next

