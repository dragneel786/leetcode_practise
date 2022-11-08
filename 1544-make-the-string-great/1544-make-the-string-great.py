class Solution:
    def makeGood(self, s: str) -> str:
        n = len(s)
        if(n == 1): return s
        
        st = deque()
        for c in s:
            if(st and c != st[-1] and \
               st[-1].lower() == c.lower()):
                st.pop()
                continue
            
            st.append(c)
        
        return "".join(st)