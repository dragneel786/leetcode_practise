class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        plist = list(pattern)
        slist = s.split()
        if(len(plist) != len(slist)):
            return False
        
        pmap = dict()
        smap = dict()
        for p, w in zip(plist, slist):
            p1 = pmap.setdefault(p, w)
            w1 = smap.setdefault(w, p)
            if(p1 != w or w1 != p):
                return False
        
        return True