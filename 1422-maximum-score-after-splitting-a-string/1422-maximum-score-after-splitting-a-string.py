class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 1 if(s[0] == '0') else 0
        ones = s.count('1') - (zeros == 0)
        ans = zeros + ones
        for c in s[1:]:
            ans = max(ans, zeros + ones)
            zeros += c == '0'
            ones -= c == '1'
            
        return ans
        
        