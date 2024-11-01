class Solution:
    def makeFancyString(self, s: str) -> str:
        st = deque()
        cons = 0
        for c in s:
            if st and st[-1] != c:
                cons = 0
                
            if cons < 2:
                st.append(c)
            
            cons += 1
        
        return ''.join(st)
            