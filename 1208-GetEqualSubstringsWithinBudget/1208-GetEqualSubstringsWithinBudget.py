# Last updated: 2/11/2026, 2:42:50 PM
1"""
2UNDERSTAND
3- Given two string s and t of the same length, and an integer maxCost
4- We want to change s to be equal to t, and that costs s[currIdx] - t[currIdx]
5- basically the ascii difference between the two chars
6
7- we must return the maximum length of a substring s that can be changed with a cost less than or equal to maxCost, if no substring can be changed we return 0
8
9
10PLAN
11- We can obviously do this with a dynamic size sliding window where our constraint metric is cost >= 0 
12- keep a left ptr, and slide a right ptr expanding window, if constraint is broken, we can add the cost of the ascii value of the left to the maxCost and keep checking subarrays, and after we have shifted into a valid window we can check its length and maintain it in a variable
13
14"""
15class Solution:
16    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
17        max_len = float('-inf')
18        currCost = 0
19        l = 0
20
21        for r in range(len(s)):
22            cost = abs(ord(s[r]) - ord(t[r]))
23            currCost += cost
24
25            while currCost > maxCost:
26                currCost -= abs(ord(s[l]) - ord(t[l]))
27                l += 1
28            
29
30            max_len = max(max_len, r - l + 1)
31
32        return max_len