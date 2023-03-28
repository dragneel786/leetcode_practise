class Solution:
    def numberOfMatches(self, n: int) -> int:
        rounds = 0
        while(n > 1):
            rounds += (n // 2)
            odd = n & 1
            n = (n // 2 + odd)
        
        return rounds
            