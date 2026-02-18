# Last updated: 2/18/2026, 11:35:38 AM
1from collections import defaultdict
2
3class Solution:
4    def arrToTuple(self, arr):
5        return tuple(arr)
6
7    def equalPairs(self, grid: List[List[int]]) -> int:
8        rows = defaultdict(int)
9        columns = defaultdict(int)
10
11        for row in grid:
12            rows[self.arrToTuple(row)] += 1
13        
14        for col in range(len(grid[0])):
15            current_col = []
16            for row in range(len(grid)):
17                current_col.append(grid[row][col])
18            columns[self.arrToTuple(current_col)] += 1
19        
20        ans = 0
21        for arr in rows:
22            ans += rows[arr] * columns[arr]
23
24        return ans
25
26
27