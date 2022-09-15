class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counts = Counter(changed)
        changed.sort()
        original = []
        
        for c in changed:
            if(counts[c]):
                original.append(c)
                counts[c] -= 1
                
                if(not counts[c * 2]):
                    return []
                
                counts[c * 2] -= 1
        
        return original
                
                
                
        
        
            
            
            
        