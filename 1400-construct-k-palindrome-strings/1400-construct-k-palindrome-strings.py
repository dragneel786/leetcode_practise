class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        counts = Counter(s)
        odd = 0
        combos = 0
        for v in counts.values():
            if(v % 2): 
                odd += 1
            
            combos += (v // 2 * 2) 
        
        return odd <= k and (k - odd) <= combos 