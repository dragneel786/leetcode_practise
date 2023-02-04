class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
#         if(m > n):
#             return False
        
        target = [0] * 26
        for c in s1:
            target[ord(c) - 97] += 1
        
        window = [0] * 26
        for i in range(n):
            if(i >= m):
                if(window == target):
                    return True
                window[ord(s2[i - m]) - 97] -= 1
            window[ord(s2[i]) - 97] += 1
            
        return target == window
        