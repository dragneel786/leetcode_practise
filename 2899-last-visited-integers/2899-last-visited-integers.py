class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        st = []
        res = []
        idx = -1
        for w in words:
            if(w == "prev"):
                val = -1
                if(idx >= 0):
                    val = st[idx]
                    idx -= 1
                res.append(int(val))
                
            else:
                st.append(w)
                idx = len(st) - 1
        
        return res
                