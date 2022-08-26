class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        def is_pow(num):
            bit_pos = 1 << int(log(num) / log(2))
            return bit_pos == num
            
        
        n = list(str(n))
        for combo in permutations(n):
            if(combo[0] == '0'): continue
            if(is_pow(int(''.join(combo)))):
                return True
            
            
            