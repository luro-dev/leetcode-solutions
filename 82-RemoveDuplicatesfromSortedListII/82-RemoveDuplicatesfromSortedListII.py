# Last updated: 3/11/2026, 9:53:14 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7"""
8- Sorted so all duplicates will be right next to each other
9- Need to check if the current number is unique
10
11"""
12class Solution:
13    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
14        dummy = ListNode(-999, head)
15        prev = dummy
16
17        while head:
18            if head.next and head.val == head.next.val:
19                while head.next and head.val == head.next.val:
20                    head = head.next
21                prev.next = head.next
22            else:
23                prev = head
24            
25            head = head.next
26              
27        
28        return dummy.next
29        