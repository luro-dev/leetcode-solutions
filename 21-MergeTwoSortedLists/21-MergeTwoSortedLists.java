// Last updated: 3/5/2026, 7:52:15 PM
1/**
2 * Definition for singly-linked list.
3 * public class ListNode {
4 *     int val;
5 *     ListNode next;
6 *     ListNode() {}
7 *     ListNode(int val) { this.val = val; }
8 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
9 * }
10 */
11class Solution {
12    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
13        ListNode dummyHead = new ListNode(-1);
14        ListNode tail = dummyHead;
15
16        while(list1 != null && list2 != null) {
17            if (list1.val < list2.val) {
18                tail.next = list1;
19                list1 = list1.next;
20            } else {
21                tail.next = list2;
22                list2 = list2.next;
23            }
24            tail = tail.next;
25        }
26
27        if (list1 != null) {
28            tail.next = list1;
29        }
30        if (list2 != null) {
31            tail.next = list2;
32        }
33
34        return dummyHead.next;
35     }
36}