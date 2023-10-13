class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = deque()
        count = 0
        for c in s:
            if(c == ')'):
                if(st):
                    st.popleft()
                else:
                    count += 1
            else:
                st.append(c)
        
        return count + len(st)
            