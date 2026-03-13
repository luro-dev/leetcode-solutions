# Last updated: 3/13/2026, 1:04:28 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7"""
8The twin node of node (i) is the node at (len(lst) - 1) - i
9- if i >= 0 and i <= (n/2) - 1
10
11- Twin sum is the sum of the ith node and its twin node
12- Given the head of a linked list with even length -> return maximum twin sum
13
14PLAN:
15- maintain a maxSum var and check each twin sum to see if greater updating accordingly
16- we can use a ptr and iterate n / 2 times and then reverse that segment, then we will have lined up the twin nodes and can loop through once
17
18IMPORTANT:
19- List length will always be even
20- Nodes will always be positive
21- There will always be at least 2 nodes
22"""
23class Solution:
24    def reverseList(self, head):
25        prev = None
26        while head:
27            next_node = head.next
28            head.next = prev
29            prev = head
30            head = next_node
31        
32        return prev
33    def pairSum(self, head: Optional[ListNode]) -> int:
34        slow = head
35        fast = head
36
37        while fast and fast.next:
38            slow = slow.next
39            fast = fast.next.next
40
41        temp = slow
42
43
44        twin_list_head = self.reverseList(temp)
45        maxTwinSum = float('-inf')
46
47        while twin_list_head:
48            maxTwinSum = max(twin_list_head.val + head.val, maxTwinSum)
49            head = head.next
50            twin_list_head = twin_list_head.next
51
52        return maxTwinSum
53