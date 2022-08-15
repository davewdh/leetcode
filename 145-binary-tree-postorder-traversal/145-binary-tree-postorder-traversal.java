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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> aList = new ArrayList<>();
        if (root == null)
            return aList;
        aList.addAll(postorderTraversal(root.left));
        aList.addAll(postorderTraversal(root.right));
        aList.add(root.val);
        return aList;
    }
}