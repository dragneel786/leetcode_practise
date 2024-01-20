class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        st = deque()
        ans, n = 0, len(arr)
        MOD = (10 ** 9) + 7
        for i, a in enumerate(arr):
            
            while(st and st[-1][0] > a):
                v, j = st.pop()
                prev_idx = st[-1][1] if(st) else -1
                ans = (ans + (v * ((j - prev_idx) * (i - j)))) % MOD
            
            st.append((a, i))
        
        
        while(st):
            v, j = st.pop()
            prev_idx = st[-1][1] if(st) else -1
            ans = (ans + (v * ((j - prev_idx) * (n - j)))) % MOD
            
        return ans
            