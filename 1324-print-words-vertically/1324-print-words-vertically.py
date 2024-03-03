class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        i = 0
        st = deque(["*"])
        res = []
        while(len(st) > 0):
            st.clear()
            for word in words:
                if(i < len(word)):
                    st.append(word[i])
                
                else:
                    st.append(' ')
            
            while(st and st[-1] == " "):
                st.pop()
            
            if(st):
                res.append("".join(st))
            i += 1
    
        return res
                
                