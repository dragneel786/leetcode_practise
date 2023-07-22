class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        switch = False
        n <<= 1
        while(n):
            switch = not switch
            n >>= 1
            if(n % 2 == 0):
                continue
                
            if(switch):
                even += 1
            else:
                odd += 1
        
        return [even, odd]
                