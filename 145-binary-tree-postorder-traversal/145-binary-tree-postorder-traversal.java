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
        Stack<TreeNode> s1 = new Stack<>();
        Stack<Integer> s2 = new Stack<>();
        List<Integer> aList = new ArrayList<>();
         if (root == null)
             return aList;
        s1.push(root);
        while (s1.size() > 0) {
            TreeNode temp = s1.pop();
            s2.push(temp.val);
            if (temp.left != null)
                s1.push(temp.left);
            if (temp.right != null)
                s1.push(temp.right);
        } 
        
        while (s2.size() > 0) {
            aList.add(s2.pop());
        }
        return aList;
        
        
        // List<Integer> aList = new ArrayList<>();
        // if (root == null)
        //     return aList;
        // aList.addAll(postorderTraversal(root.left));
        // aList.addAll(postorderTraversal(root.right));
        // aList.add(root.val);
        // return aList;
    }
}