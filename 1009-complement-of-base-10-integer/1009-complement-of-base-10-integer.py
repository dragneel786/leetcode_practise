class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if(not n): return 1
        
        bits = int(log(n) / log(2)) + 1
        return (1 << bits) - n - 1
            
            
            