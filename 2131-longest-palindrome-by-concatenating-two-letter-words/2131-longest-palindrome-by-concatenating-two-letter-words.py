class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        wcounts = Counter(words)
        length = 0
        single = 0
        print(wcounts)
        for key, value in wcounts.items():
            rkey = key[::-1]
            if(key == rkey):
                mul = value // 2
                length += (4 * mul)
                wcounts[key] -= (mul * 2)
                if(wcounts[key] == 1):
                    single = 2
            
            elif(wcounts[rkey]):
                minv = min(value, wcounts[rkey])
                length += (4 * minv)
                wcounts[key] -= minv
                wcounts[rkey] -= minv
        
        return length + single
        
        
        
                
            
                
            
        
        