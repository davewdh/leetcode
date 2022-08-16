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
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length < 1)
            return null;
        int mid = nums.length/2;
        TreeNode root = new TreeNode(nums[mid]);
        int[] arr1 = Arrays.copyOfRange(nums, 0, mid);
        int[] arr2 = Arrays.copyOfRange(nums, mid+1, nums.length);
        root.left = sortedArrayToBST(arr1);
        root.right = sortedArrayToBST(arr2);
        return root;
    }
}