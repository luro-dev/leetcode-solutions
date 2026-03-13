# Last updated: 3/13/2026, 1:24:10 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7"""
8- We are given head, which is a reference to a singly linked list, the value in each node is either 0 or 1 and its not empty. 
9- The LL holds the binary representation of a number
10
11- We can reverse the list to get the LSB at the start then just loop through accumulating with a number and doing 2^count * node.val and add it to the total
12"""
13class Solution:
14    def getDecimalValue(self, head: Optional[ListNode]) -> int:
15        prev = None
16        while head:
17            n = head.next
18            head.next = prev
19            prev = head
20            head = n
21        
22        number = 0
23        deg = 0
24        while prev:
25            number += (2 ** deg) * prev.val
26            deg += 1
27            prev = prev.next
28
29        return number