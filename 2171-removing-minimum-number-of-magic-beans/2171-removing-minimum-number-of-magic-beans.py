class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        return sum(beans) - max((len(beans) - i) * b\
                               for i, b in enumerate(sorted(beans)))
        
        
        
            
        
        