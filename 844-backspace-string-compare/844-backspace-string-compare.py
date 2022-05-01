class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def construct(s):
            res = ""
            count = 0
            for i in range(len(s) - 1, -1, -1):
                if(s[i] != "#"):
                    if(count):
                        count -= 1
                        continue
                    res = s[i] + res
                else:
                    count += 1
            return res
                
            
        s = construct(s)
        t = construct(t)
        return s == t