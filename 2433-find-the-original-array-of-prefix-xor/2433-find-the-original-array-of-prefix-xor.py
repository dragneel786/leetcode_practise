class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        prev = 0
        for i, p in enumerate(pref):
            res.append(prev ^ p)
            prev = p
        
        return res
            
        
        
        