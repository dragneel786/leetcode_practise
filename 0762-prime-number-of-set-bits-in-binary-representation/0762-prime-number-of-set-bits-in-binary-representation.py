class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isprime(val):
            if(val == 2):
                return True
            
            for d in range(2, ceil(sqrt(val)) + 1):
                if(val % d == 0):
                    return False
                
            return val != 1
        
        primes = {i for i in range(1, 32) if(isprime(i))}
        res = 0
        for num in range(left, right + 1):
            count = 0
            while(num):
                count += (num & 1)
                num >>= 1
            
            res += (count in primes)
        
        return res
        
        