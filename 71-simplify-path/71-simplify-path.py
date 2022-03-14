class Solution:
    def simplifyPath(self, path: str) -> str:
        st = deque()
        path += "/"
        val = ""
        for c in path:
            if(c == "/"):
                if(val == ".."):
                    if(len(st)):
                        st.pop()
                elif(val != "." and val != ""):
                    st.append(val)
                val = ""
            else:
                val += c

        return "/" + "/".join(st)