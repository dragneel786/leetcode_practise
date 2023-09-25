class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = Counter(s)
        for c in t:
            if(c not in counter_s):
                return c
            
            counter_s[c] -= 1
            if(not counter_s[c]):
                del counter_s[c]
        
        return list(counter_s.keys())[0]