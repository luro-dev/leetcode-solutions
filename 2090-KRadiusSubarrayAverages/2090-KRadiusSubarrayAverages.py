# Last updated: 2/10/2026, 6:20:15 PM
1"""
2So we want to build an array of averages that holds the average of all the numbers k units left and k units right of some index, if there are less than k elements before or after the index then we can declare the k-radius average for that index to be -1
3
4basically, construct a prefix sum since we will be calculating averages for every valid index, then iterate through every index and calculate the average using the prefix sum array, this is constant time since we know we have k elements to the left and right + 1 for current index, so its 2k+1 elements
5
6
7"""
8
9class Solution:
10    def getAverages(self, nums: List[int], k: int) -> List[int]:
11        prefix = [nums[0]]
12        res = []
13        for i in range(1, len(nums)):
14            prefix.append(nums[i] + prefix[-1])
15        
16
17        for idx in range(len(nums)):
18            if (idx - k < 0) or (idx + k >= len(nums)):
19                res.append(-1)
20            else:
21                sub_sum = prefix[idx + k] if (idx - k - 1) < 0 else prefix[idx + k] - prefix[idx - k - 1]
22                res.append(sub_sum // (2*k + 1))
23
24        return res
25