# Last updated: 3/14/2026, 11:31:24 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        if not head: return head
10
11        evenHead = head.next
12
13        oddTemp = head
14        evenTemp = evenHead
15
16        while evenTemp and evenTemp.next:
17            oddTemp.next = evenTemp.next
18            oddTemp = oddTemp.next
19            
20            evenTemp.next = oddTemp.next
21            evenTemp = evenTemp.next
22            
23        oddTemp.next = evenHead
24
25        return head
26       