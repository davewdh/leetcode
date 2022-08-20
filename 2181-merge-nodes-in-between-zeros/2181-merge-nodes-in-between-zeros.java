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
    public ListNode mergeNodes(ListNode head) {
        ListNode node = new ListNode(-1);
        ListNode current = node;
        int sum = 0;
        while (head != null) {
            if (head.val == 0 && sum != 0) {
                current.next = new ListNode(sum);
                current = current.next;
                sum = 0;
                continue;
            }
            
            sum += head.val;
            head = head.next;
        }
        return node.next;
    }
}