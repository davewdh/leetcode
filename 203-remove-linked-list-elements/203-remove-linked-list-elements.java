/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode root = new ListNode();
        ListNode current = root;
        while (head != null) {
            if (head.val != val) {
                current.next = new ListNode(head.val);
                current = current.next;
            }
            head = head.next;
        }
        return root.next;
    }
}