# Last updated: 2/10/2026, 5:14:59 PM
1"""
2- We are given a list of numbers, there will be a start value, this value added to the running sum should never allow the total sum to reach anything under 1
3
4[-3,2,-3,4,2]
5[-3, -1, -4, 0, 2]
61 - (-4)
71 + 4 = 5
8min prefix 
9abs + 1
10
11we know if the minimum prefix sum is negative we need to shift the array by the absolute value of the minimum sum + 1 to make sure its >= 1
12
13if its positivve we know the minimum value can be 1 since there are no positive values that can decrease the sum, anything greater than 1 would mean a greater step by step sum
14"""
15
16
17class Solution:
18    def minStartValue(self, nums: List[int]) -> int:
19        prefix = [nums[0]]
20        min_val = nums[0]
21        for i in range(1, len(nums)):
22            prefix.append(prefix[-1] + nums[i])
23            min_val = min(min_val, prefix[-1])
24        
25        if min_val < 1:
26            return abs(min_val) + 1
27        else:
28            return 1
29        
30
31        
32        