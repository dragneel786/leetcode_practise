class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        ham_dis = 0
        while(x or y):
            val = (x ^ y) & 1
            ham_dis += val == 1
            if(x): x >>= 1
            if(y): y >>= 1
        
        return ham_dis
            