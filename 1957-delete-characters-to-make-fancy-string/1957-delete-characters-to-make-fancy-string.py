class Solution:
    def makeFancyString(self, s: str) -> str:
        st = deque()
        cons = 1
        for c in s:
            if st and st[-1] != c:
                cons = 1
                
            if cons < 3:
                st.append(c)
            
            cons += 1
        
        return ''.join(st)
            