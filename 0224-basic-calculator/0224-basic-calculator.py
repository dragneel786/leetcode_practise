class Solution:
    def calculate(self, s: str) -> int:
        
        def evaluate():
            if(not st or type(st[-1]) == str):
                st.append(0)
            
            res = st.pop()
            while(st and st[-1] != ')'):
                op = st.pop()
                if(op == '+'):
                    res += st.pop()
                else:
                    res -= st.pop()
            
            return res
            
                
        
        st = deque()
        n = operand = 0
        for c in s[::-1]:
            if(c.isdigit()):
                val = int(c) * (10 ** n)
                n += 1
                st.append(val + (st.pop() if(st and n > 1) else 0))
        
            elif(c != ' '):
                n = 0
                if(c == '('):
                    res = evaluate()
                    st.pop()
                    st.append(res)
                else:
                    st.append(c)
        
        return evaluate()
                
            
                