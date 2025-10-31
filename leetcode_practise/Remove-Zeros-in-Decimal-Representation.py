class Solution:
    def removeZeros(self, n: int) -> int:
        rev = 0
        while(n):
            rem = n % 10
            n //= 10
            if rem == 0:
                continue
                
            rev = (rev * 10) + rem
            
        
        return int(str(rev)[::-1])