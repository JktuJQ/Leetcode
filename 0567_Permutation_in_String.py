from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        seen = defaultdict(int)
        for i in range(len(s1)):
            seen[s1[i]] -= 1
            seen[s2[i]] += 1
            if seen[s1[i]] == 0:
                del seen[s1[i]]
            if seen[s2[i]] == 0:
                del seen[s2[i]]
        if len(seen) == 0:
            return True

        start = 0
        for _ in range(len(s2) - len(s1)):
            seen[s2[start]] -= 1
            if seen[s2[start]] == 0:
                del seen[s2[start]]
            i = start + len(s1)
            seen[s2[i]] += 1
            if seen[s2[i]] == 0:
                del seen[s2[i]]
            if len(seen) == 0:
                return True
            start += 1
        return False
