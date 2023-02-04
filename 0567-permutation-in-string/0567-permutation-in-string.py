class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        target = [0] * 26
        window = [0] * 26
        for c, a in zip(s1, s2):
            window[ord(a) - 97] += 1
            target[ord(c) - 97] += 1
        
        for i in range(m, n):
            if(window == target):
                return True
            window[ord(s2[i - m]) - 97] -= 1
            window[ord(s2[i]) - 97] += 1
            
        return m <= n and target == window
        