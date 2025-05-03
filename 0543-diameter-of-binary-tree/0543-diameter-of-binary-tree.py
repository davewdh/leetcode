# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        if not root:
            return 0
        
        def dfs(node): # return height
            if not node:
                return 0
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            self.ans = max(self.ans, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return self.ans
