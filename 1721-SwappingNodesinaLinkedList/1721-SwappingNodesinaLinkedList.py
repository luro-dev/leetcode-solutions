# Last updated: 3/12/2026, 11:35:25 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
9        first = head
10        second = head
11        current = head
12
13        for i in range(1, k):
14            first = first.next
15
16        current = first
17
18        while current.next:
19            current = current.next
20            second = second.next
21
22        first.val, second.val = second.val, first.val
23
24        return head