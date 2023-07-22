class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        switch = False
        while(n):
            if(n % 2 == 1):
                if(switch):
                    odd += 1
                else:
                    even += 1
            
            switch = not switch
            n >>= 1
        
        return [even, odd]
                