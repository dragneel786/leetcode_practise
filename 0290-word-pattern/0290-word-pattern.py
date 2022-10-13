class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split()
        if(len(pattern) != len(slist)):
            return False
        
        pmap = dict()
        smap = dict()
        for p, w in zip(pattern, slist):
            p1 = pmap.setdefault(p, w)
            w1 = smap.setdefault(w, p)
            if(p1 != w or w1 != p):
                return False
        
        return True