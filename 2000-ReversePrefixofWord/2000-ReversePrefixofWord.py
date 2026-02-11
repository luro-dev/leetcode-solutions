# Last updated: 2/11/2026, 12:59:53 PM
1class Solution:
2    def reversePrefix(self, word: str, ch: str) -> str:
3        ch_list = list(word)
4        
5        return word if ch not in ch_list else self.reverseSection(ch_list, 0, ch_list.index(ch)) 
6
7
8    def reverseSection(self, arr, start_idx, end_idx):
9        left = 0
10        right = end_idx
11
12        while left < right:
13            arr[left], arr[right] = arr[right], arr[left]
14            left += 1
15            right -= 1
16
17        return "".join(arr)