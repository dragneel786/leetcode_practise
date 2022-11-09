class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = -1
        while(n):
            curr = n & 1
            if(prev != -1 and prev == curr):
                return False
            
            prev = curr
            n >>= 1
        
        return True
        