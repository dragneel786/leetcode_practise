class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ans = []
        idx = 0
        n = len(part)
        part = list(part)
        for c in s:
            ans.append(c)
            size = len(ans)
            if(size >= n and part == ans[size - n:]):
                for _ in range(n):
                    ans.pop()

        return ''.join(ans)
                
            
                
                
            
            