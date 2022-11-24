class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        st = deque()
        for c in s:
            if(c.isalpha()):
                st.append(c)
        
        res = []
        for c in s:
            if(not c.isalpha()):
                res.append(c)
            else:
                res.append(st.pop())
        
        return ''.join(res)