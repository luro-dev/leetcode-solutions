# Last updated: 3/12/2026, 12:02:09 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7"""
8- Iterate to middle of linked list.
9- Reverse the second half, then iterate from the head of the first list and head of second list, if any value differs the LL is not a palindrome
10"""
11class Solution:
12    def isPalindrome(self, head: Optional[ListNode]) -> bool:
13    
14        fast = head
15        slow = head
16
17        while fast and fast.next:
18            slow = slow.next
19            fast = fast.next.next
20        
21        curr = slow
22        prev = None
23
24        while curr:
25            nxt = curr.next
26            curr.next = prev
27            prev = curr
28            curr = nxt
29        
30        while prev:
31            if head.val != prev.val:
32                return False
33            head = head.next
34            prev = prev.next
35        
36        return True
37
38