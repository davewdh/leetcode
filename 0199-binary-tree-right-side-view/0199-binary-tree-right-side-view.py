# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = collections.deque([root])

        while q:
            l = len(q)
            rightMost = None
            for i in range(l):
                node = q.popleft()
                if node:
                    rightMost = node.val
                    q.append(node.left)
                    q.append(node.right)
            if rightMost is not None:
                ans.append(rightMost)
        return ans
