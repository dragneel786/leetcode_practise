class Solution:
    def romanToInt(self, s: str) -> int:
        romans_value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        res = romans_value[s[0]]
        prev = res
        for i, c in enumerate(s[1:], 1):
            val = romans_value[s[i]]
            res += val
            if(prev < val):
                res -= (2 * prev)
            prev = val
        
        return res
                
                
            