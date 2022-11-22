class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isprime(val):
            if(val == 2):
                return True
            
            for d in range(2, val):
                if(val % d == 0):
                    return False
                
            return val != 1
        
        # primes = {i for i in range(1, (10 ** 6) + 1) if(isprime(i))}
        res = 0
        for num in range(left, right + 1):
            count = 0
            while(num):
                count += (num & 1)
                num >>= 1
            
            res += (isprime(count))
        
        return res
        
        