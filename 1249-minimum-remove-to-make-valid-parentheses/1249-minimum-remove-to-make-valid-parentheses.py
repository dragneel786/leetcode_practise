class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = deque()
        s = list(s)
        for i in range(len(s)):
            if(s[i] == "("):
                st.append(i)
            elif(s[i] == ")"):
                if(not len(st)):
                    s[i] = "_"
                else:
                    st.pop()
        
        while(len(st)):
            s[st.pop()] = "_"
        
        ans = ""
        for i in range(len(s)):
            if(s[i] == "_"):
                continue
            ans += s[i]
        
        return ans
                