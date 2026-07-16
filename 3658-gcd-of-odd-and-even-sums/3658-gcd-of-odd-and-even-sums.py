class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return gcd(n * n, n * (n + 1))
    
    def gcd(self, a: int, b: int) -> int:
        if a == 1 or b == 1:
            return max(a, b)
            
        if a < b:
            return gcd(a, b//a)
        else:
            return gcd(b, a//b)

