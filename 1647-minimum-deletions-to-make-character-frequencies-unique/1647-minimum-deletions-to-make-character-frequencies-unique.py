class Solution:
    def minDeletions(self, s: str) -> int:
        C = Counter(s)
        dele = 0
        uniq = set()
        keys = C.keys()
        for ki in keys:
            while(C[ki] in uniq and C[ki]):
                C[ki] -= 1
                dele += 1
            uniq.add(C[ki])
            
        return dele
                
                    
                