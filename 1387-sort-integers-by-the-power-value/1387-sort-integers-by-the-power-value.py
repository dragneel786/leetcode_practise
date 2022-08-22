class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def get_steps_count(val):
            if(val == 1): return 1
            
            if(val in memo): return memo[val]
            
            ret =  get_steps_count(val * 3 + 1) if(val & 1)\
            else get_steps_count(val // 2)
            
            memo[val] = ret + 1
            return memo[val]
        
        memo = {}
        res = [(get_steps_count(num), num) for num in range(lo, hi + 1)]
        res.sort()
        return res[k - 1][1]
        
        
        