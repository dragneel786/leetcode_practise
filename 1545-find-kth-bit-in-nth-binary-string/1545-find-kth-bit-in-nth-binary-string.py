class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def rev_bits(values):
            for i in range(len(values)):
                values[i] = '1' if values[i] == '0' else '0'
            
            return values
            
        
        s = ["0"]
        for _ in range(n):
            s = s + ["1"] + rev_bits(s[:])[::-1]
            # print(s)
            if len(s) >= k:
                break
            
            
        
        return s[k - 1]