# Last updated: 3/12/2026, 1:32:12 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7"""
8- Given the head of a linked list. 
9- The nodes of the list are assigned to groups, who have lengths of the sequence of natural numbers (1st group 1 node , 2nd group 2 nodes, 3rd group 3 nodes, etc.)
10- We want to reverse the nodes of the groups with even lengths
11- Remember the edge case for the last group, must check its length it may be less than or equal to the length of the 2nd to last group 
12
13
14- Use a counter variable starting at 1 and increment it every move, keep a pointer to the head of the previous group, this will connect to the newHead of new group, and also track previousHead since it will be the tail that will connect to next group
15
16IMPORTANT:
17- oldGroupTail
18- newGroupHead
19- currentGroupHead
20
21if reversed curr group, currGroupHead becomes its tail and a prev Value becomes new head so:
22    oldGroupTail.next = currGroupPrev
23    currentGroupHead.next = newGroupHead
24
25
26"""
27class Solution:
28    # reverse group and return the new head
29    def reverseGroup(self, head):
30        prev = None
31        while head:
32            next_node = head.next
33            head.next = prev
34            prev = head
35            head = next_node
36        return prev
37    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
38        group_num = 2
39        curr = head
40        while curr.next:
41            group_count = 1
42            temp = curr.next
43
44            while group_count < group_num and temp.next:
45                group_count += 1
46                temp = temp.next
47
48            if group_count % 2 == 0:
49                groupStart = curr.next
50                nextGroupHead = temp.next 
51
52                groupEnd = temp
53                groupEnd.next = None
54
55                newHead = self.reverseGroup(groupStart)
56                curr.next = newHead
57                groupStart.next = nextGroupHead
58
59                curr = groupStart
60            else:
61                curr = temp
62
63            group_num += 1
64
65        return head
66            
67
68
69        
70        