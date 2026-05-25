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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1 == null){
            return list2;
        }else if(list2 == null){
            return list1;
        }else if(list1.val<list2.val){
            ListNode head = list1;
            head.next = mergeTwoLists(list1.next,list2);
            return head;
        }else{
            ListNode head = list2;
            head.next = mergeTwoLists(list1,list2.next);
            return head;
        }
    }
}