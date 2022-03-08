class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        shift = 1
        for i in range(32):
            if(shift & n):
                count += 1
            shift <<= 1
        
        return count