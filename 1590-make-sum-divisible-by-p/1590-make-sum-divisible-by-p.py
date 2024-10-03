class Solution:
    def minSubarray(self, A: List[int], p: int) -> int:
        need = sum(A) % p
        dp = {0: -1}
        cur = 0
        res = n = len(A)
        # print(need)
        for i, a in enumerate(A):
            cur = (cur + a) % p
            dp[cur] = i
            # print("curr", cur, "res", res, "dp", dp)
            if (cur - need) % p in dp:
                # print("mod", cur, need, f'{(cur - need) % p}')
                res = min(res, i - dp[(cur - need) % p])
        return res if res < n else -1
            
            
            
                
                
            
        
            
        