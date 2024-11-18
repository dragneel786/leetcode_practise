class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        def get_sum(idx):
            val = 0
            if k == 0:
                return 0
            
            d = -1 if k < 0 else 1
            idx += d
            for _ in range(abs(k)):
                if idx < 0:
                    idx = len(code) - 1
                elif idx >= len(code):
                    idx = 0
                
                # print(i)
                val += code[idx]
                idx += d
            
            return val
                
        n = len(code)
        res = [0] * n
        for i in range(n):
            res[i] = get_sum(i)
        
        return res