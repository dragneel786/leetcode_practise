class Solution:
    def makeFancyString(self, s: str) -> str:
        st = deque()
        for c in s:
            if len(st) > 1 and st[-2] == st[-1] == c:
                continue
            
            st.append(c)
        
        return ''.join(st)