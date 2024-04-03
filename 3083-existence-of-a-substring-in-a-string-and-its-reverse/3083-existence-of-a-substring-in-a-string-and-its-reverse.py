class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev_s = s[::-1]
        for start in range(len(s)):
            for end in range(start + 1, len(s)):
                if(s[start: end + 1] in rev_s):
                    return True
        
        return False
        