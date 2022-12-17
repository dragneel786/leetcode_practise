class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = deque()
        for c in tokens:
            if(c.lstrip('-').isdigit()):
                st.append(c)
            else:
                b, a = st.pop(), st.pop()
                val = int(eval(a + c + b))
                st.append(str(val))
        
        return int(st.pop())
            