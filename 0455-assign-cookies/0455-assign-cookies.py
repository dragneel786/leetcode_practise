class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = len(s)
        count = idx = 0
        for greed in g:
            while(idx < n and greed > s[idx]):
                idx += 1
            
            if(idx >= n):
                break
            
            count += 1
            idx += 1
        
        return count