class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opmap = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        st = deque()
        for ch in tokens:
            if(ch.lstrip("-").isnumeric()):
                st.append(ch)
            else:
                b = int(st.pop())
                a = int(st.pop())
                st.append(opmap[ch](a, b))

        return int(st.pop())