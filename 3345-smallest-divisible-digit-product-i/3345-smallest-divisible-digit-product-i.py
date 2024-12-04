class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def is_div(num):
            pro = 1
            while(num):
                pro *= (num % 10)
                num //= 10
            
            return pro % t == 0
        
        while(not is_div(n)):
            n += 1
        
        return n
            
            