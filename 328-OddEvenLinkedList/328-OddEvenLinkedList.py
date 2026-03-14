# Last updated: 3/14/2026, 11:29:30 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7"""
8- Given a list like 1 -> 2 -> 3 -> 4 -> 5
9- Group all odd index nodes with each other then all even nodes, maintain order
10- Use counter starting at 1 and check odd / even with mod
11
12- Two pointers, one for odd lst one for even, connecting .next.next 
13"""
14class Solution:
15    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
16        if not head: return head
17
18        evenHead = head.next
19
20        oddTemp = head
21        evenTemp = evenHead
22
23        while oddTemp and oddTemp.next and evenTemp and evenTemp.next:
24            oddTemp.next = evenTemp.next
25            oddTemp = oddTemp.next
26            evenTemp.next = oddTemp.next
27            evenTemp = evenTemp.next
28            
29        oddTemp.next = evenHead
30
31        return head
32       