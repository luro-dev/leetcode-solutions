# Last updated: 3/9/2026, 8:09:58 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode(-1, head)
9
10        prev = dummy
11        fast = head
12        slow = head
13    
14        while fast and fast.next:
15            prev = prev.next
16            slow = slow.next
17            fast = fast.next.next
18        
19        prev.next = slow.next
20
21        return dummy.next
22