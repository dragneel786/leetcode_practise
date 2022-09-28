class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        ham_dis = 0
        
        while(xor):
            xor &= (xor - 1)
            ham_dis += 1
        
        return ham_dis
            