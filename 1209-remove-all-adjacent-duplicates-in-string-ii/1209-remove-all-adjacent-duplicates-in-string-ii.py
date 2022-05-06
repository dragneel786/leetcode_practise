class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = deque()
        for c in s:
            if(len(st) and st[-1][0] == c):
                val = [c, st[-1][1] + 1]
                st.append(val)
                if(val[1] == k):
                    for _ in range(k):
                        st.pop()
            else:
                val = [c, 1]
                st.append(val)
        
        res = ""
        while(len(st)):
            res = st.pop()[0] + res
        
        return res