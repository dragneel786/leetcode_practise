class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        zeros = s.count('0')
        max_len = zeros
        
        val = 0
        for i, c in enumerate(s[::-1]):
            if(c != '0'):
                val += (1 << i)
                if(val > k):
                    return max_len
                
                max_len += 1
        
        return max_len
            
        
        
    
        
            