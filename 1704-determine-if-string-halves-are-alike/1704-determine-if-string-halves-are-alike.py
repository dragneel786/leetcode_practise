class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vcount = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        n = len(s)
        
        for i, c in enumerate(s):
            c = c.lower()
            if(c in vcount and i < n // 2):
                vcount[c] += 1
            
            elif(c in vcount):
                vcount[c] -= 1
        
        return sum(vcount.values()) == 0