class Solution:
    def makeFancyString(self, s: str) -> str:
        st = deque()
        cons = 1
        for c in s:
            # print(st, c)
            if not st:
                st.append(c)
                continue
                
            if st[-1] == c:
                cons += 1
            else:
                cons = 1
            
            if cons < 3:
                st.append(c)
        
        return ''.join(st)
            