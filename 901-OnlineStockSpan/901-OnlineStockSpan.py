# Last updated: 4/2/2026, 12:46:07 PM
1class StockSpanner:
2
3    def __init__(self):
4        self.stack = [] # pair (price, span)
5        
6
7    def next(self, price: int) -> int:
8        span = 1
9        while self.stack and self.stack[-1][0] <= price:
10            span += self.stack.pop()[1]
11        self.stack.append((price, span))
12
13        return self.stack[-1][1]
14
15
16# Your StockSpanner object will be instantiated and called as such:
17# obj = StockSpanner()
18# param_1 = obj.next(price)