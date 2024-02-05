class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res = curr = 0
        seen = {0: -1}
        for i, c in enumerate(s):
            curr ^= 1 << ('aeiou'.find(c) + 1) >> 1
            seen.setdefault(curr, i)
            res = max(res, i - seen[curr])
            # print(seen, seen[curr])
        
        return res