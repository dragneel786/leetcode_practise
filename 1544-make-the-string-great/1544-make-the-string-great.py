class Solution:
    def makeGood(self, s: str) -> str:
        st = deque()
        for c in s:
            if(not st or c.lower() != st[-1].lower() \
               or c.islower() == st[-1].islower() \
               or st[-1].isupper() == c.isupper()):
                st.append(c)
             
            else:
                st.pop()
        
        return ''.join(st)
    