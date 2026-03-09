# Last updated: 3/9/2026, 7:31:17 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
9        dummyHead = ListNode(-1, head)
10
11        before_rev = None
12        rev_start = None
13
14
15        curr = head
16        prev = dummyHead
17        idx = 1
18
19        while idx != left:
20            prev = curr
21            curr = curr.next
22            idx += 1
23        
24        before_rev = prev
25        rev_start = curr
26        rev_tail = rev_start
27        rev_prev = None
28
29        while idx <= right:
30            nxt = rev_start.next
31            rev_start.next = rev_prev
32            rev_prev = rev_start
33            rev_start = nxt
34            idx += 1
35
36        rev_tail.next = rev_start
37        before_rev.next = rev_prev
38
39        return dummyHead.next
40            
41    
42
43
44
45
46