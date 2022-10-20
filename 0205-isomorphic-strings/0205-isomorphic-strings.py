class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def transform(word):
            ret = []
            cmap = dict()
            for i, c in enumerate(word):
                ret.append(cmap.setdefault(c, str(i)))
            
            return " ".join(ret)
                
        
        return transform(s) == transform(t)
                
            