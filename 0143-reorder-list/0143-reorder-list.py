# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        l, r = 0, len(nodes) - 1
        while l < r:
            nodes[l].next = nodes[r]
            l = l + 1
            if l >= r:
                break
            nodes[r].next = nodes[l]
            r = r - 1
        nodes[l].next = None