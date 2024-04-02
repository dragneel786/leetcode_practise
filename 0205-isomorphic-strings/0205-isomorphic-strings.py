class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1, map2 = {}, {}
        for a, b in zip(s, t):
            if(a not in map1):
                map1[a] = b
            
            if(b not in map2):
                map2[b] = a
            
            if(map1[a] != b or map2[b] != a):
                return False
    
        return True
        