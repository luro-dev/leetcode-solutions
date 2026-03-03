# Last updated: 3/3/2026, 12:32:34 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode(0, head)
9        curr = head
10
11        while curr and curr.next:
12            if curr.val == curr.next.val:
13                curr.next = curr.next.next
14            else:
15                curr = curr.next
16        
17        return dummy.next