# Last updated: 4/2/2026, 1:27:37 PM
1"""
2- Given a string s, which contains letters and *'s, we can choose a star in s, and remove the closest non-star char to the left as well as itself
3- We want to remove the string after all stars have been removed
4"""
5
6class Solution:
7    def removeStars(self, s: str) -> str:
8        stack = []
9        strings = []
10        for char in s:
11            if char == "*":
12                stack.append(char)
13            else:
14                strings.append(char)
15
16            while stack and strings:
17                stack.pop()
18                strings.pop()
19        
20        return "".join(strings) if len(strings) > 0 else ""
21            