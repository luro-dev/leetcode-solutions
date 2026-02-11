# Last updated: 2/11/2026, 6:19:26 PM
1"""
2- This seems like a prefix sums problem
3- We have (n + 1) points at different altitudes, we start at point 0, altitude 0
4- Given an array of length n, arr[i] is the gain in altitude between i and i+1
5"""
6
7class Solution:
8    def largestAltitude(self, gain: List[int]) -> int:
9        prefix = [0]
10
11        for i in range(len(gain)):
12            prefix.append(prefix[-1] + gain[i])
13
14        return max(prefix)