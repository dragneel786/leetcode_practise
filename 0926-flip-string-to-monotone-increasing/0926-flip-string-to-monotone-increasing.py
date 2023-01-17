class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        z = 0
        for c in s:
            z += c == '0'
        
        ans = z
        for c in s:
            if(c == '0'):
                z -= 1
                ans = min(ans, z)
            else:
                z += 1
        
        return ans
                
                    
                    