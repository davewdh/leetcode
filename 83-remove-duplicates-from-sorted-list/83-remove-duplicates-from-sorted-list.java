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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode root = head;
        
        while (root != null) {
            if (root.next == null)
                break;
            if (root.val == root.next.val) {
                root.next = root.next.next;
            } else {
                root = root.next;
            } 
        }
        return head;  
        
        
        // if (head == null)
        //     return head;
        // if (head.next == null)
        //     return head;
        // head.next = deleteDuplicates(head.next);
        // return (head.val == head.next.val) ? head.next : head;
    
    }
}