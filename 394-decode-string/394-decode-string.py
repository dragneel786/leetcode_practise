class Solution:
    def decodeString(self, s: str) -> str:
        st = deque()
        for c in s:
            if(c == "]"):
                t = ""
                while(not st[-1].isdigit()):
                    p = st.pop()
                    if(p == "["):
                        continue
                    t = p + t
                st.append(int(st.pop()) * t)
            else:
                if(st and st[-1].isdigit() and c.isdigit()):
                    st.append(st.pop() + c)
                else:
                    st.append(c)
        
        res = ""
        while(st):
            res = st.pop() + res
        return res