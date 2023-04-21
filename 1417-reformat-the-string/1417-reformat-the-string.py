class Solution:
    def reformat(self, S: str) -> str:
        d = []
        s = []
        for c in S:
            if(c.isdigit()):
                d.append(c)
            else:
                s.append(c)
        
        
        def make_string(a, b):
            return ''.join([a + b for a, b in \
                            zip_longest(a, b, fillvalue="")])
        
        
        if(abs(len(d) - len(s)) > 1):
            return ""
        
        if(len(d) > len(s)):
            return make_string(d, s)
        else:
            return make_string(s, d)
        