# Last updated: 4/6/2026, 5:39:25 PM
1"""
2- order to push and order to pop
3- popped and pushed have same lenth, all numbers are distinct
4- maintain idx to know what ele to pop next in sequence
5- go through numbers in pushed appending to stack if we encounter popped number in sequence pop it and increment the i counter, we could pop multiple times so use while loop, 
6- if we get through all numbers and stack is empty it was valid, if there is stuff on the stack it was not
7"""
8
9class Solution:
10    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
11        stack = []
12        idx = 0
13        for num in pushed:
14            stack.append(num)
15            while idx < len(popped) and stack and popped[idx] == stack[-1]:
16                stack.pop()
17                idx += 1
18
19        return not stack