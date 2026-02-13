# Last updated: 2/12/2026, 7:41:12 PM
1class Solution:
2    def checkIfPangram(self, sentence: str) -> bool:
3        return len(set(sentence)) == 26