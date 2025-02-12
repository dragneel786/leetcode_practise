class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st = []
        part = list(part)
        psize = len(part)
        for c in s:
            st.append(c)
            if len(st) >= psize and st[len(st) - psize:] == part:
                for _ in range(psize):
                    st.pop()
        
        return ''.join(st)