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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null)
            return null;
        int sum = ((l1 == null) ? 0 : l1.val) + ((l2 == null) ? 0 : l2.val);
        ListNode head = new ListNode(sum % 10);
        head.next = addTwoNumbers((l1 == null) ? null : l1.next, (l2 == null) ? null : l2.next);
        if (sum >= 10) 
            head.next = addTwoNumbers(head.next, new ListNode(1));
        return head;
    }
}