# Last updated: 2/10/2026, 8:27:15 PM
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        split_words = s.split()
4        res = []
5        for word in split_words:
6            res.append(self.reverseWord(word))
7        
8        return " ".join(res)
9
10    def reverseWord(self, word):
11        word_arr = list(word)
12
13        left = 0 
14        right = len(word_arr) - 1
15
16        while left < right:
17            word_arr[right], word_arr[left] = word_arr[left], word_arr[right]
18            left += 1
19            right -= 1
20
21
22        return "".join(word_arr)