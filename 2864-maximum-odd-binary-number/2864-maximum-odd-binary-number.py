class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        ones = 0
        for c in s:
            ones += (c == '1')
        
        zeros = len(s) - ones
        ones -= 1
        return (ones * "1") + (zeros * "0") + '1'