# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0

            if node.val >= maxVal:
                ans = 1
            else:
                ans = 0
            maxVal = max(node.val, maxVal)
            ans += dfs(node.left, maxVal)
            ans += dfs(node.right, maxVal)
            return ans 
        return dfs(root, root.val)