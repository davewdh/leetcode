# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        
        index = count - n #3
        if index == 0:
            return head.next

        cur2 = head
        for i in range(count - 1):  # 1, 2, 3, 4 ,5
            if (i + 1) == index:
                cur2.next = cur2.next.next
                break
            cur2 = cur2.next
        
        return head