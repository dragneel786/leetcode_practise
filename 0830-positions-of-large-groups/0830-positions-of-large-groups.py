class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start = 0
        ans = []
        s += '-'
        for i in range(1, len(s)):
            if(s[start] != s[i]):
                if(i - start >= 3):
                    ans.append([start, i - 1])
                start = i
        
        return ans
                
            
            
            