class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counts = Counter(changed)
        if(counts[0] % 2): return []

        for c in sorted(counts):
            if(counts[c] > counts[2 * c]):
                return []
            counts[2 * c] -= counts[c] if(c) else counts[c] // 2

        return list(counts.elements())
                
                
                
        
        
            
            
            
        