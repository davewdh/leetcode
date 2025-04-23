"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyMap = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            copyMap[cur] = copy
            cur = cur.next
        
        cur2 = head
        while cur2:
            copy2 = copyMap[cur2]
            copy2.next = copyMap[cur2.next]
            copy2.random = copyMap[cur2.random]
            cur2 = cur2.next
        return copyMap[head]