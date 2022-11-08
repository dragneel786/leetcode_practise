class Solution:
    def makeGood(self, s: str) -> str:
        n = len(s)
        if(n == 1): return s
        
        st = deque([chr(0)])
        for c in s:
            if(abs(ord(st[-1]) - ord(c)) == 32):
                st.pop()
                continue
            
            st.append(c)
        
        st.popleft()
        return "".join(st)