class Solution:
    def minSteps(self, s: str, t: str) -> int:
        tcounts = Counter(t)
        for c in s:
            if(tcounts[c]):
                tcounts[c] -= 1
        
        return sum(tcounts.values())