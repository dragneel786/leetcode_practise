class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candis = {i for i in range(1, n + 1)}
        trusted = [0] * (n + 1)
        for a, b in trust:
            candis.discard(a)
            trusted[b] += 1
        
        val = None
        if(len(candis) == 1):
            val = list(candis)[0]
        
        return -1 if(not val or trusted[val] < (n - 1)) else val 