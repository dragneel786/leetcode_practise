class Solution:
    def decodeString(self, s: str) -> str:
        st = deque()
        for c in s:
            if(c != "]"):
                if(st and st[-1].isdigit() and c.isdigit()):
                    st[-1] += c
                else:
                    st.append(c)
                continue
            
            t = ""
            while(not st[-1].isdigit()):
                p = st.pop()
                if(p == "["):
                    continue
                t = p + t
            st.append(int(st.pop()) * t)
        
        return "".join(st)