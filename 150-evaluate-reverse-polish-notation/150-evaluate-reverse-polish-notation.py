class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = deque()
        for ch in tokens:
            if(ch.lstrip("-").isnumeric()):
                st.append(ch)
            else:
                b = int(st.pop())
                a = int(st.pop())
                if(ch == "+"):
                    res = a + b
                elif(ch == "-"):
                    res = a - b
                elif(ch == "*"):
                    res = a * b
                else:
                    res = a / b
                st.append(res)

        return int(st.pop())