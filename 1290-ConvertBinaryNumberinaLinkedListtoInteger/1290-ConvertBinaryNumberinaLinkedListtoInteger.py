# Last updated: 3/13/2026, 1:37:49 PM
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
15        num = 0
16
17        while head:
18            num = (2 * num) + head.val
19            head = head.next
20        
21        return num