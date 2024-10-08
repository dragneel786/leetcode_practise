class Solution:
    def minSwaps(self, s: str) -> int:
        s = list(s)
        op = 0
        n = len(s)
        end = n - 1
        swaps = 0
        for start, c in enumerate(s):
            if c == '[':
                op += 1
                continue
                
            while(end > start and s[end] != '['):
                end -= 1
            
            if end <= start:
                break
            
            if(op == 0):
                s[start], s[end] = s[end], s[start]
                swaps += 1
                op += 1
            else:
                op -= 1
        
        return swaps