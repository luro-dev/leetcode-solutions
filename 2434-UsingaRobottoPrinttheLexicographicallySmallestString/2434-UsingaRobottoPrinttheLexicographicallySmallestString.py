# Last updated: 4/3/2026, 11:22:03 AM
1"""
2- Apply operations until s and t (strings) are empty
3
4- Remove first character of ( S ) and give it to robot to append to string ( T )
5- Remove last character of ( T ) and give it to the robot to write on paper
6
7- lexographically smallest is a string that would appear first in a dictionary
8
9-- Count of chars,
10-- add to stack and at each addition decide if pop
11-- if there is no character after the curr char that is lexographically less add to paper
12-- greedy choice at each spot
13"""
14from collections import defaultdict
15class Solution:
16    def robotWithString(self, s: str) -> str:
17        c = defaultdict(int)
18        for x in s: c[x] += 1
19
20        min_char = 'a'
21        p = []
22        t = []
23
24        for ch in s:
25            t.append(ch)
26            c[ch] -= 1
27
28            while min_char != 'z' and c[min_char] == 0:
29                min_char = chr(ord(min_char) + 1)
30            while t and t[-1] <= min_char:
31                p.append(t.pop())
32
33        return "".join(p)