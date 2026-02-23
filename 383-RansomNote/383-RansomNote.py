# Last updated: 2/23/2026, 5:45:37 PM
1from collections import Counter
2
3"""
4- My idea is that I can make a counter of the magazine string and then iterate through the letters of the ransomNote, if I reach a letter I check if its in the magazine letter count and if it is I decrease it's count, if its not I return false since we don't have the letter to construct the note.
5
6"""
7class Solution:
8    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
9        magazine_letter_count = Counter(magazine)
10    
11        for char in ransomNote:
12            if char in magazine_letter_count:
13                if magazine_letter_count[char] == 0:
14                    return False
15                else:
16                    magazine_letter_count[char] -= 1
17            else:
18                return False
19    
20        return True