class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        res = []
        for values in zip_longest(*words, fillvalue=" "):
            values = list(values)
            while(values[-1] == ' '):
                values.pop()
            
            res.append("".join(values))
    
        return res
            
                
                