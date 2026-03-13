# Last updated: 3/13/2026, 1:10:39 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7"""
8- Given the head of a linked list and an integer val
9- Remove all nodes from the list that have a value == val
10
11
12- Need a dummy to head in case head must be removed
13- Loop through while keeping reference to prev and if curr node matches update prev to prev.next = curr.next
14
15IMPORTANT:
16- head can be empty
17- pos int vals
18- val to check can be 0
19"""
20class Solution:
21    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
22        dummy = ListNode(-1, head)
23        prev = dummy
24        curr = head
25
26        while curr:
27            if curr.val == val:
28                curr = curr.next
29                prev.next = curr
30            else:
31                prev = curr
32                curr = curr.next
33        
34        return dummy.next
35                
36                
37            
38            