class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = deque()
        for c in tokens:
            if(c.lstrip('-').isdigit()):
                st.append(c)
            else:
                b, a = st.pop(), st.pop()
                st.append(str(int(eval(a + c + b))))
        
        return int(st.pop())
            