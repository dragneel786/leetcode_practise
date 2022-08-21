class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Algorithm.
        # Get gcd number with length and check the string 1 with string 2
        def gcd(m, n):
            if(not n): return m
            return gcd(n, m % n)
        
        m, n = len(str1), len(str2)
        size = gcd(m, n)
        res = str1[:size]
        
        if(res * (m // size) == str1\
           and res * (n // size) == str2):
            return res
        
        return ""
        