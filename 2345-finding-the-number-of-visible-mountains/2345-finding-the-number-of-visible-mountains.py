class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        st = deque()
        peaks.sort()
        
        def is_hidden(pa, pb):
            x1, y1 = pa
            x2, y2 = pb
            return x1 - y1 >= x2 - y2 and\
        x1 + y1 <= x2 + y2
        
        for peak in peaks:
            overlap = False
            
            while(st and is_hidden(st[-1], peak)):
                if(st[-1] == peak):
                    overlap = True
                
                st.pop()
            
            if(overlap or (st and is_hidden(peak, st[-1]))):
                continue
            
            st.append(peak)
        
        return len(st)
        