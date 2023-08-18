class Solution:
    def minTimeToType(self, word: str) -> int:
        seconds = 0
        curr = 0
        for c in word:
            cidx = ord(c) - 97
            seconds += 1
                
            if(cidx < curr):
                seconds += min(curr - cidx, (26 - curr) + cidx)
            
            elif(cidx > curr):
                seconds += min(cidx - curr, (26 - cidx) + curr)
            
            curr = cidx
        
        return seconds
            
                
        
        