# Last updated: 4/2/2026, 1:36:33 PM
1"""
2- Given a string s, which contains letters and *'s, we can choose a star in s, and remove the closest non-star char to the left as well as itself
3- We want to remove the string after all stars have been removed
4"""
5
6class Solution:
7    def removeStars(self, s: str) -> str:
8        stack = []
9        for char in s:
10            if char == "*":
11                if stack:
12                    stack.pop()
13            else:
14                stack.append(char)
15        
16        return "".join(stack) if len(stack) > 0 else ""
17            