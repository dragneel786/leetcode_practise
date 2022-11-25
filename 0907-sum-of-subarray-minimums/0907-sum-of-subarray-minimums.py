class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = (10 ** 9) + 7
        st = deque()
        res = 0
        for i, a in enumerate(arr):

            while(st and st[-1][0] > a):
                v, j = st.pop()
                res += (((j - st[-1][1]) if(st) else j + 1) * (i - j) * v)

            st.append((a, i))

        while(st):
            v, j = st.pop()
            res += (((j - st[-1][1]) if(st) else j + 1) * (len(arr) - j) * v)

        return res % MOD
        
            
            