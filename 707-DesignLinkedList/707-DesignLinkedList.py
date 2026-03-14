# Last updated: 3/14/2026, 12:23:50 PM
1class ListNode:
2    def __init__(self, value, next_node=None):
3        self.val = value
4        self.next = next_node
5
6class MyLinkedList:
7
8    def __init__(self):
9        self.head = None
10        self.tail = None
11        self.size = 0
12
13    def get(self, index: int) -> int:
14        if index >= self.size:
15            return -1
16        
17        if index < 0:
18            return self.head.val
19
20        temp = self.head
21        for i in range(index):
22            temp = temp.next
23        
24        return temp.val
25    def addAtHead(self, val: int) -> None:
26        if self.size == 0:
27            self.head = ListNode(val)
28            self.tail = self.head
29            self.size += 1
30        else:
31            newNode = ListNode(val, self.head)
32            self.head = newNode
33            self.size += 1
34
35    def addAtTail(self, val: int) -> None:
36        if self.size == 0:
37            newNode = ListNode(val)
38            self.head = newNode
39            self.tail = self.head
40            self.size +=1
41        else:
42            newNode = ListNode(val)
43            self.tail.next = newNode
44            self.tail = newNode
45            self.size +=1
46
47    def addAtIndex(self, index: int, val: int) -> None:
48        if index > self.size: return None
49        if index <= 0: return self.addAtHead(val)
50        if index == self.size: return self.addAtTail(val)
51
52        temp = self.head
53        newNode = ListNode(val)
54        counter = 0
55
56        while temp and counter != index - 1:
57            temp = temp.next
58            counter += 1
59        
60        newNode = ListNode(val, temp.next)
61        temp.next = newNode
62        self.size += 1
63
64    def deleteAtIndex(self, index: int) -> None:
65        if index < 0 or index >= self.size: return None
66        if self.size == 0: return None
67
68        if index == 0: 
69            self.head = self.head.next
70            self.size -= 1
71            if self.size == 0:
72                self.tail = self.head
73            return None
74
75
76        temp = self.head
77        counter = 0
78        while temp and counter != index - 1:
79            temp = temp.next
80            counter += 1
81
82        if self.size - 1 == index:
83            temp.next = None
84            self.tail = temp
85        else:
86            temp.next = temp.next.next
87        self.size -= 1
88
89
90# Your MyLinkedList object will be instantiated and called as such:
91# obj = MyLinkedList()
92# param_1 = obj.get(index)
93# obj.addAtHead(val)
94# obj.addAtTail(val)
95# obj.addAtIndex(index,val)
96# obj.deleteAtIndex(index)