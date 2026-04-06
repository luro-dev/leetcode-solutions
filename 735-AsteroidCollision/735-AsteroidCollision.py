# Last updated: 4/6/2026, 6:39:51 PM
1"""
2- Use difference, if pos wins then set a = 0
3- if pos loses pop from stack, 
4- if diff = 0 pop and set a to 0
5- at the end only add the asteroid if it won everything
6"""
7class Solution:
8
9
10    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
11        stack = []
12
13        for a in asteroids:
14            while stack and a < 0 and stack[-1] > 0:
15                diff = stack[-1] + a
16
17                if diff < 0:
18                    stack.pop()
19                elif diff > 0:
20                    a = 0
21                else:
22                    stack.pop()
23                    a = 0
24            
25            if a != 0:
26                stack.append(a)
27
28
29        return stack