class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        wcounts = Counter(words)
        length = single = 0
        
        for key, count in wcounts.items():
            rkey = key[::-1]
            minv = 0
         
            if(wcounts[rkey]):
                minv = min(count, wcounts[rkey])
                
                if(key == rkey):
                    if(minv & 1):
                        single = 2
                    minv //= 2
                    
                wcounts[key] = wcounts[rkey] =  0 
            length += (4 * minv)
        
        return length + single
        
        
        
                
            
                
            
        
        