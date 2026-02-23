# Last updated: 2/23/2026, 5:55:28 PM
1"""
2- So we cantg to return the count of stones that we have that are jewels
3- We get a str, that tells us which stone types are also jewels (hash this for O(1) lookups)
4- Since letters are case sensitive make sure to not change cases, iterate through stones we have and check if they are in the jewel lookup, if they are increment counter.
5
6"""
7class Solution:
8    def numJewelsInStones(self, jewels: str, stones: str) -> int:
9        num_jewel_stones = 0
10
11        jewels_hashed = set(jewels)
12
13        for stone in stones:
14            if stone in jewels_hashed:
15                num_jewel_stones += 1
16
17        return num_jewel_stones