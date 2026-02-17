# Last updated: 2/17/2026, 9:51:28 AM
1from collections import defaultdict
2"""
3UNDERSTAND
4- Given an int arr MATCHES where MATCHES[i] = [WINNER:i, LOSER:i]
5- Return a list of size 2 where: ans[0] = list of all players with NO LOSSES
6- ans[1] = list of all players that have lost EXACTLY ONE MATCH
7- Should be returned in INCREASING ORDER
8
9PLAN
10- Use hashmap, count wins,
11- Iterate through hashmap appending to proper index of ans
12- Sort each list in ans
13"""
14
15class Solution:
16    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
17        lose_count = defaultdict(int)
18        ans = [[], []]
19
20        for match in matches:
21            loser = match[1]
22            winner = match[0]
23
24            lose_count[loser] += 1
25            lose_count[winner] += 0
26        
27        for player, losses in lose_count.items():
28            if losses == 0:
29                ans[0].append(player)
30            elif losses == 1:
31                ans[1].append(player)
32            
33        ans[0].sort()
34        ans[1].sort()
35
36        return ans