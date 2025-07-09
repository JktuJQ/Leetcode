from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = list()
        if len(p) > len(s):
            return indices

        seen = defaultdict(int)
        for i in range(len(p)):
            seen[p[i]] -= 1
            seen[s[i]] += 1
            if seen[p[i]] == 0:
                del seen[p[i]]
            if seen[s[i]] == 0:
                del seen[s[i]]

        start = 0
        if len(seen) == 0:
            indices.append(start)
        for _ in range(len(s) - len(p)):
            seen[s[start]] -= 1
            if seen[s[start]] == 0:
                del seen[s[start]]

            i = start + len(p)
            seen[s[i]] += 1
            if seen[s[i]] == 0:
                del seen[s[i]]
            
            start += 1
            if len(seen) == 0:
                indices.append(start)
        return indices
