# Last updated: 2/17/2026, 10:45:11 AM
1from collections import defaultdict
2"""
3UNDERSTAND
4- Given a binary array (arr containing only 0 or 1), return the length of the longest subarray where there are an equal number of 0's and 1's
5
6PLAN
7- So this is similar to subarray sum equal to k, we have no way of knowing when the subarray begins with just a sliding window and the constraint has a strict numeric restriction.
8- We can use a hashmap to store a index of the sum, if we see a 1 add it to curr else remove a 1, if we have a previous sum that would equal 0 if we subtracted it from our current sum we know its a valid index, we can then
9- We can return 0 if ans is equal to our guard value to indicate that there was no subarray with equal number of 0's and 1's
10"""
11
12class Solution:
13    def findMaxLength(self, nums: List[int]) -> int:
14        ans = float('-inf')
15        curr = 0
16        prefix_map = defaultdict(int)
17        prefix_map[0] = -1
18
19        for r in range(len(nums)):
20            if nums[r] == 1:
21                curr += 1
22            else:
23                curr -= 1
24
25            if curr in prefix_map:
26                ans = max(ans, r - prefix_map[curr])
27            
28            if curr not in prefix_map:
29                prefix_map[curr] = r
30            
31        return ans if ans != float('-inf') else 0