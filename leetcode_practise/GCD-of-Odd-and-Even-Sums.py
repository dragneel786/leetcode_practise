class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = sum_even = 0
        start = 1
        for _ in range(n):
            sum_odd += start
            sum_even += start + 1
            start += 2
        
        def get_gcd(a, b):
            if b == 0:
                return a
            
            return get_gcd(b, a % b)
        
        return get_gcd(sum_even, sum_odd)
            
