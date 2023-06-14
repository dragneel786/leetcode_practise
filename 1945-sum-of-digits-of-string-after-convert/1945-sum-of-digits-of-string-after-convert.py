class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        def sums(num):
            nonlocal val
            while(num):
                val += (num % 10)
                num //= 10
        
        val = 0
        for c in s:
            sums(ord(c) - 96)
        
        
        for _ in range(k-1):
            temp = val
            val = 0
            sums(temp)
        
        return val
        
        
        
        