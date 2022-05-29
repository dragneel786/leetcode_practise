class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        s1 = Counter(s)
        s2 = Counter(t)
        for k in s:
            if(s1.get(k, 0) != s2.get(k, 0)):
                return False
        
        return 0 == 0