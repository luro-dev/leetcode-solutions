# Last updated: 4/3/2026, 10:06:26 AM
1class MyQueue:
2
3    def __init__(self):
4        self.s1 = []
5        self.s2 = []
6
7    def push(self, x: int) -> None:
8        self.s1.append(x)
9
10    def pop(self) -> int:
11        if self.s2:
12            return self.s2.pop()
13        elif self.s1:
14            while self.s1:
15                self.s2.append(self.s1.pop())
16
17            return self.s2.pop()
18
19    def peek(self) -> int:
20        if self.s2:
21            return self.s2[-1]
22        elif self.s1:
23            while self.s1:
24                self.s2.append(self.s1.pop())
25
26            return self.s2[-1]
27
28    def empty(self) -> bool:
29        return not self.s2 and not self.s1
30        
31
32
33# Your MyQueue object will be instantiated and called as such:
34# obj = MyQueue()
35# obj.push(x)
36# param_2 = obj.pop()
37# param_3 = obj.peek()
38# param_4 = obj.empty()