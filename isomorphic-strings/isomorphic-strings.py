class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cmap = dict()
        for a, b in zip(s, t):
            if('a' + a in cmap and cmap['a' + a] != b):
                return False
            
            if('b' + b in cmap and cmap['b' + b] != a):
                return False
            
            cmap['a' + a] = b
            cmap['b' + b] = a
        
        return True
                
            