class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ones = 0
        for c in s:
            ones += c == '1'
        
        return ((ones - 1) * '1') + ((n - ones) * '0') + '1'