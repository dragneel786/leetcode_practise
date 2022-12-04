class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        st = deque()
        for a in arr:
            if(not a):
                st.append(0)
                st.append(0)
            else:
                st.append(a)
            
            if(len(st) >= len(arr)):
                break
        
        i = 0
        while(i < len(arr)):
            arr[i] = st.popleft()
            i += 1