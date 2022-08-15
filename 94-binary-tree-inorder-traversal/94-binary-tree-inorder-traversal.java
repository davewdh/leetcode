/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> aList = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        if (root == null)
            return aList;
        TreeNode current = root;
        while (current != null || stack.size() > 0) {
            if (current != null) {
                stack.push(current);
                current = current.left;
            } else {
                current = stack.pop();
                aList.add(current.val);
                current = current.right;
            }
        }
        return aList;
        
        // List<Integer> arr = new ArrayList<>();
        // if (root == null) 
        //     return arr;
        // arr.addAll(inorderTraversal(root.left));
        // arr.add(root.val);
        // arr.addAll(inorderTraversal(root.right));
        // return arr;
        
        
        
        
        
        
        
        
        
        
        
    }
}