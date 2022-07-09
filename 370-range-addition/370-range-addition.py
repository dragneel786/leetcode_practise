class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * (length + 1)
        for u in updates:
            s, e, inc = u
            res[s] += inc
            res[e + 1] -= inc
            
        for i in range(1, length + 1):
            res[i] += res[i - 1]
        
        return res[:-1]