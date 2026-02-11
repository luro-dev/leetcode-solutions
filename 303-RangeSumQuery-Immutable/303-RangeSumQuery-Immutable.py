# Last updated: 2/11/2026, 6:41:16 PM
1class NumArray:
2
3    def __init__(self, nums: List[int]):
4        self.prefix = [nums[0]]
5        for i in range(1, len(nums)):
6            self.prefix.append(self.prefix[-1] + nums[i])
7       
8
9    def sumRange(self, left: int, right: int) -> int:
10        if left == 0:
11            return self.prefix[right]
12        else:
13            return self.prefix[right] - self.prefix[left - 1]
14
15
16# Your NumArray object will be instantiated and called as such:
17# obj = NumArray(nums)
18# param_1 = obj.sumRange(left,right)