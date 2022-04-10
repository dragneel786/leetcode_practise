class Solution:
    def calPoints(self, ops: List[str]) -> int:
        st = deque()
        for o in ops:
            if(o == '+'):
                st.append(st[-1] + st[-2])
            elif(o == 'D'):
                st.append(st[-1] * 2)
            elif(o == "C"):
                st.pop()
            else:
                st.append(int(o))
        
        return sum(st)