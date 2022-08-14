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
    public boolean isPalindrome(ListNode head) {
        ListNode current = head;
        Stack<Integer> aStack = new Stack<>();
        while (current != null) {
            aStack.push(current.val);
            current = current.next;
        }
        
        current = head;
        int size = 0;
        while (size <= aStack.size()/2) {
            if (aStack.pop() != current.val) 
                return false;
            else
                current = current.next;
            size += 1;
        }
        return true;
        
    }
}