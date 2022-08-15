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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> aList = new ArrayList<>();
        if (root == null) 
            return aList;
        aList.add(root.val);
        aList.addAll(preorderTraversal(root.left));
        aList.addAll(preorderTraversal(root.right));
        return aList;
    }
}