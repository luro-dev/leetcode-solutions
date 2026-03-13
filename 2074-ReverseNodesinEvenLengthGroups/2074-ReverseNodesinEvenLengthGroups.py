# Last updated: 3/13/2026, 12:07:06 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7"""
8- We want to reverse only the groups that have an even length, 
9- The groups will be in order sequentially forming the sequence of natural nums
10- 1st group 1 node, 2nd 2 nodes, last group can be variable so we have to check len
11
12- keep a temp to iterate through the group 
13- curr will always point to prev tail
14- iterate temp until group_count is 1 less than group_num to get the curr group tail
15- always save next groupHead, and set the current groupTail.next to null to establish end point for reversal
16- if the group count is odd just make sure that curr = temp since we just want to shift curr to the current tail
17- if the group is even reverse it, the oldhead will be the new tail so connect that to the nextGroupHead and the old tail will now be the new head so make sure to connect curr.next to oldTail
18- always increment the group_num by one at the end
19"""
20class Solution:
21    def reverseHelper(self, head):
22        prev = None
23        while head:
24            next_node = head.next
25            head.next = prev
26            prev = head
27            head = next_node
28        
29        return prev
30
31    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
32        dummy = ListNode(-999, head)
33        curr = head
34        group_num = 2
35
36        while curr.next:
37            temp = curr
38            group_count = 0
39
40            while temp.next and group_count < group_num:
41                temp = temp.next
42                group_count += 1
43            
44            if group_count % 2 == 0:
45                next_group_head = temp.next
46                
47                group_head = curr.next
48                group_tail = temp
49                group_tail.next = None
50
51                newHead = self.reverseHelper(group_head)
52
53                curr.next = newHead
54                group_head.next = next_group_head
55                curr = group_head
56            else:
57                curr = temp
58            
59            group_num += 1
60
61        return dummy.next