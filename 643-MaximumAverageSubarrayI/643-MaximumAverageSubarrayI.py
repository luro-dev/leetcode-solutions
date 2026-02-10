# Last updated: 2/9/2026, 7:19:53 PM
1"""
2- This is a sliding window problem, we are asked to find a subarray of size k, that has the highest maximum average value of all size k subarrays, this is a fixed size sliding window problem
3
4- At every iteration we remove one element from the left and add one from the right then divide by / k to caluclate the average value of the current subarray in constant time
5
6- We can create the first average value since k <= n
7"""
8class Solution:
9    def findMaxAverage(self, nums: List[int], k: int) -> float:
10        runningSum = 0
11        for i in range(k):
12            runningSum += nums[i]
13
14        currentAverage = runningSum / k
15        maxAverage = currentAverage
16
17        for right in range(k, len(nums)):
18            currentNum = nums[right]
19            previousNum = nums[right - k]
20
21            runningSum = (runningSum - previousNum) + currentNum
22
23            currentAverage = runningSum / k
24
25            maxAverage = max(currentAverage, maxAverage)
26
27        return maxAverage
28        