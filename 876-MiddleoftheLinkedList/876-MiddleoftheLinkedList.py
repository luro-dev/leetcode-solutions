# Last updated: 3/3/2026, 12:27:01 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        slow = head
9        fast = head
10
11        while fast and fast.next:
12            slow = slow.next
13            fast = fast.next.next
14
15        return slow