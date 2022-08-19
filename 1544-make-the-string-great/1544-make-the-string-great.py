class Solution:
    def makeGood(self, s: str) -> str:
        
        check_validity = lambda a, b: ((a.islower() and b.isupper()) or\
        (a.isupper() and b.islower())) and (a.lower() == b.lower())
        
        st = deque([s[0]])
        for c in s[1:]:
            
            if(st and check_validity(st[-1], c)):
                st.pop()
                
            else:
                st.append(c)
        
        return "".join(st)