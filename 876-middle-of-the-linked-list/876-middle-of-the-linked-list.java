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
    public ListNode middleNode(ListNode head) {
        ListNode first = head;
        ListNode second = head;
        while (second != null && second.next != null) {
            first = first.next;
            second = second.next.next;
        }
        return first;
        
        
//         if (head ==  null)
//             return null;
//         if (head.next == null)
//             return head;
        
//         ListNode current = head;
//         int count = 0;
//         while (current != null) {
//             count++;
//             current = current.next;
//         }
        
//         current = head;
//         for (int i = 0; i< (int)Math.ceil(count/2); i++) {
//             current = current.next;
//         }
//         return current;
        
    }
}