# Last updated: 2/11/2026, 6:21:33 PM
1"""
2- This seems like a prefix sums problem
3- We have (n + 1) points at different altitudes, we start at point 0, altitude 0
4- Given an array of length n, arr[i] is the gain in altitude between i and i+1
5
6- We start at alt 0, so we can start a prefix sum with a start of 0 and return the maximum height since that will be the highest altitude of a point
7"""
8
9class Solution:
10    def largestAltitude(self, gain: List[int]) -> int:
11        prefix = [0]
12
13        for i in range(len(gain)):
14            prefix.append(prefix[-1] + gain[i])
15
16        print(prefix)
17        return max(prefix)