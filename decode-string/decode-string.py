class Solution:
    def decodeString(self, s: str) -> str:
        
        def pop_and_create():
            temp = ''
            while(st[-1] != '['):
                temp = st.pop() + temp

            st.pop()
            st.append(int(st.pop()) * temp)

        st = deque()
        for c in s:
            if(c == ']'):
                pop_and_create()
            else:
                if(st and st[-1].isdigit() and c.isdigit()):
                    st.append(st.pop() + c)
                else:
                    st.append(c)

        return ''.join(st)