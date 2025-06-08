class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def gen_order(curr):
            nonlocal res, n
            for start in range(10):
                val = (curr * 10) + start
                if val == 0:
                    continue
                    
                if val > n:
                    return
                
                res.append(val)
                gen_order(val)
        
        
        res = []
        gen_order(0)
        return res