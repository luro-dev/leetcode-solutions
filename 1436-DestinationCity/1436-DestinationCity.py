# Last updated: 2/24/2026, 12:42:49 PM
1"""
2Understand:
3- Given an array paths, where each index of path contains two cities with paths between them.
4- Return the only city with no outgoing path
5
6Plan 
7- From what I see I just count cities and the city with a frequency of 1 is the end city
8
9"""
10class Solution:
11    def destCity(self, paths: List[List[str]]) -> str:
12        has_outgoing = set()
13
14        for path in paths:
15            departing_from = path[0]
16            if departing_from not in has_outgoing:
17                has_outgoing.add(departing_from)
18
19        for path in paths:
20            destination = path[1]
21
22            if destination not in has_outgoing:
23                return destination