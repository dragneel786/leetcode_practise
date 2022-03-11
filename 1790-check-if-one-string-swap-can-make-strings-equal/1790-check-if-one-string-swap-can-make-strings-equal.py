class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = 0
        w1 = [0] * 26
        w2 = [0] * 26
        for i in range(len(s1)):
            if(s1[i] != s2[i]):
                diff += 1
            w1[ord(s1[i]) - 97] += 1
            w2[ord(s2[i]) - 97] += 1
        
        return diff == 0 or (diff == 2 and w1 == w2)