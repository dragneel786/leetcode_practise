class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        res = 0
        for num in range(left, right + 1):
            count = 0
            while(num):
                num &= (num - 1)
                count += 1
            
            res += (count in primes)
        
        return res
        
        