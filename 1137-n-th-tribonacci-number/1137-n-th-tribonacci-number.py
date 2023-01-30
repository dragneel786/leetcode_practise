class Solution:
    def tribonacci(self, n: int) -> int:
        
        def get_trib(s):
            if(s < 3):
                return 1 if(s > 0) else 0
            
            if(s in memo):
                return memo[s]
            
            ret = get_trib(s - 1) + \
            get_trib(s - 2) + get_trib(s - 3)
            
            memo[s] = ret
            return ret
        
        memo = {}
        return get_trib(n)