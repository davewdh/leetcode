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
        ListNode head = new ListNode();
        ListNode current = head;
        int carry = 0;
        while (l1 != null || l2 != null) {
            int sum = ((l1 == null) ? 0 : l1.val) + ((l2 == null) ? 0 : l2.val) + carry;
            carry = sum / 10;
            
            current.next = new ListNode(sum % 10);
            current = current.next;
            l1 = (l1 == null) ? null : l1.next;
            l2 = (l2 == null) ? null : l2.next;
        }
        if (carry != 0)
            current.next = new ListNode(1);
        
        return head.next;
        
        
        // if (l1 == null && l2 == null)
        //     return null;
        // int sum = ((l1 == null) ? 0 : l1.val) + ((l2 == null) ? 0 : l2.val);
        // ListNode head = new ListNode(sum % 10);
        // head.next = addTwoNumbers((l1 == null) ? null : l1.next, (l2 == null) ? null : l2.next);
        // if (sum >= 10) 
        //     head.next = addTwoNumbers(head.next, new ListNode(1));
        // return head;
    }
}