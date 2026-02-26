# Last updated: 2/25/2026, 8:29:04 PM
1"""
2UNDERSTAND
3- Given an positive integer arr and a pos integer k,
4- Return the length of the longest good subarray
5- A good subarray is one where the frequency of each element is <= k
6
7PLAN
8- So we need to count the frequency of each element
9- Sliding window since k is a fixed value if we add an element we check if the constraint has been met else continue, if constraint is broken we remove from the left until valid again
10"""
11from collections import defaultdict
12class Solution:
13    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
14        freq_map = defaultdict(int)
15        left = 0
16        max_sub = 0
17
18        for right in range(len(nums)):
19            num = nums[right]
20            freq_map[num] += 1
21
22            while freq_map[num] > k:
23                freq_map[nums[left]] -= 1
24                left += 1
25            
26            max_sub = max(max_sub, right - left + 1)
27
28        return max_sub