class Solution:
    def greatestLetter(self, s: str) -> str:
        string_set = set(s)
        ans = ''
        for c in s:
            if(c.isupper()):
                if(c.lower() in string_set and c > ans):
                    ans = c
        
        return ans