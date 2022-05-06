class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = deque()
        for c in s:
            if(len(st) and st[-1][0] == c):
                val = st.pop()
                val[1] += 1
                st.append(val)
                if(val[1] == k):
                    st.pop()
            else:
                val = [c, 1]
                st.append(val)
        
        res = ""
        while(len(st)):
            val = st.pop()
            res = (val[0] * val[1]) + res
        
        return res