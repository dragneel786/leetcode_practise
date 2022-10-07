class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        odd = 0
        counts = Counter(s)
        for v in counts.values():
            if(v & 1):
                odd += 1
            
                if(odd > 1): 
                    return False
        
        return True
        
        
    