class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        @lru_cache(None)
        def bills(i, var):
            if(i == len(rods)):
                if not var:
                    return 0
                
                return -inf
            
            op1 = rods[i] + bills(i + 1, var + rods[i])
            op2 = bills(i + 1, var - rods[i])
            op3 = bills(i + 1, var)
            return max(op1, op2, op3)
        
        return bills(0,0)