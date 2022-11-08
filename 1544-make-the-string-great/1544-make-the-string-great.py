class Solution:
    def makeGood(self, s: str) -> str:
        n = len(s)
        if(n == 1): return s
        
        st = deque()
        for c in s:
            if(st and abs(ord(st[-1]) - ord(c)) == 32):
                st.pop()
                continue
            
            st.append(c)
        
        return "".join(st)