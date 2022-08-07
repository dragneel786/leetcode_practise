class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if(not n): return 1
        
        bits = int(log(n) // log(2) + 1)
        res = 0
        
        for i in range(bits):
            next_bit = ((n & 1) ^ 1) << i
            res = next_bit + res 
            n >>= 1
        
        return res
            
            
            