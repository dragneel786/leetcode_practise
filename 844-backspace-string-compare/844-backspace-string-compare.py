class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def construct(s):
            res = []
            for i in s:
                if(i != "#"):
                    res.append(i)
                else:
                    if(res):
                        res.pop()
            return "".join(res)
                
            
        s = construct(s)
        t = construct(t)
        return s == t