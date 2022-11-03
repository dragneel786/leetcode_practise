class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        wcounts = Counter(words)
        length = single = 0
        
        for key, value in wcounts.items():
            rkey = key[::-1]
            minv = 0
         
            if(wcounts[rkey]):
                if(key == rkey):
                    minv = value // 2
                    single = 2 if(wcounts[key] - (minv * 2)) else single
                else:
                    minv = min(value, wcounts[rkey])
                
                wcounts[key] -= minv
                wcounts[rkey] -= minv
                
            length += (4 * minv)
        
        return length + single
        
        
        
                
            
                
            
        
        