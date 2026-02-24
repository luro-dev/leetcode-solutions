# Last updated: 2/24/2026, 12:54:51 PM
1class Solution:
2    def isPathCrossing(self, path: str) -> bool:
3        x = 0
4        y = 0
5        visited = set()
6        units = {
7            'N': 1,
8            'S': -1,
9            'E': +1,
10            'W': -1
11        }
12
13        for unit in path:
14            visited.add((x, y))
15
16            if unit == 'N' or unit == 'S':
17                y += units[unit]
18            else:
19                x += units[unit]
20
21            if (x, y) in visited:
22                return True
23
24        return False