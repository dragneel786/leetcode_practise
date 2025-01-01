class Solution:
    def maxScore(self, s: str) -> int:
        right_ones = 0
        for c in s:
            right_ones += c == '1'
        
        left_zeros = 0
        max_res = 0
        for c in s[:-1]:
            left_zeros += c == '0'
            right_ones -= c == '1'
            max_res = max(max_res, left_zeros + right_ones)
        
        return max_res