class Solution:
    def minLength(self, s: str) -> int:
        st = deque()
        for c in s:
            if(st and st[-1] + c in ['AB', 'CD']):
                st.pop()
            else:
                st.append(c)
        
        return len(st)