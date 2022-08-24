class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        def is_valid(val):
            s1 = set([1, 8, 0])
            s2 = set([1, 8, 0, 2, 5, 6, 9])
            s = set([int(c) for c in str(val)])
            return not s.issubset(s1) and s.issubset(s2)
        
        
        counts = 0
        for num in range(n + 1):
            counts += is_valid(num)
        
        return counts