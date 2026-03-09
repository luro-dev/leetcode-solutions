# Last updated: 3/9/2026, 7:56:57 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
8        dummy = ListNode(-1, head)
9        before_rev = dummy
10        idx = 0
11
12        while idx != left - 1:
13            before_rev = before_rev.next
14            idx += 1
15        idx += 1
16
17        rev_start = before_rev.next
18        curr = rev_start
19        rev_prev = None
20
21        while idx <= right:
22            nextNode = curr.next
23            curr.next = rev_prev
24            rev_prev = curr
25            curr = nextNode
26
27            idx += 1
28
29        rev_start.next = curr
30        before_rev.next = rev_prev
31
32        return dummy.next
33