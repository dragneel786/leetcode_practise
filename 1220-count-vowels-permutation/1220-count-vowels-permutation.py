class Solution:
    def countVowelPermutation(self, n: int) -> int:
        M = (10 ** 9) + 7
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            a, e, i, o, u = e, (a + i) % M, (a + e + o + u) % M, (i + u) % M, a
        return sum((a, e, i, o, u)) % M
        
            