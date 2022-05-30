class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend >= 0) == (divisor >= 0)
        if(dividend == -(1<<31) and abs(divisor) == 1):
            return (1 << 31) - 1 if sign else -(1 << 31) 
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while(dividend - divisor >= 0):
            count = 0
            while(dividend - (divisor << 1 << count) >= 0):
                count += 1
            result += 1 << count
            dividend -= divisor << count
        
        return result if sign else -result
            
                