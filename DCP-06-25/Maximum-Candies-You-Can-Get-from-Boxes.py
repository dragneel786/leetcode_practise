class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = deque()
        for c in s:
            if(c != ')'):
                st.append(c)
                
            else:
                temp = []
                while(st[-1] != '('):
                    temp.append(st.pop())
                
                st.pop()
                for v in temp:
                    st.append(v)
        
        return ''.join(st)
                    
                
                    
                    
                
            
            