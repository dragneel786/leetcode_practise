class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if(a > b):
            return self.commonFactors(b, a)
        
        count = 1
        for v in range(2, a + 1):
            count += ((a % v) == (b % v) == 0)
        
        return count