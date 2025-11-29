class Solution:
    def minimumFlips(self, n: int) -> int:
        orig = bin(n)[2:]
        rev = orig[::-1]
        res = 0
        for a, b in zip(orig, rev):
            res += (a != b)
        
        return res