class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = deque(['#'])
        for c in s:
            if(st[-1] == c):
                st.pop()
            else:
                st.append(c)
        
        st.popleft()
        return "".join(st)