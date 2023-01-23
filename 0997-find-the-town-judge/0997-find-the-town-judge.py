class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_to = [0] * (n + 1)
        trust_by = [0] * (n + 1)
        for a, b in trust:
            trust_to[b] += 1
            trust_by[a] += 1
        
        ans = -1
        for i in range(1, n + 1):
            if(trust_to[i] == (n - 1) and trust_by[i] == 0):
                ans = i
        
        return ans