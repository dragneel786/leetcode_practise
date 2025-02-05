class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_idx = []
        for i, (a, b) in enumerate(zip(s1, s2)):
            if a != b:
                diff_idx.append(i)
            
            if len(diff_idx) > 2:
                return False

        if len(diff_idx) == 2:
            i, j = diff_idx
            if s1[i] == s2[j] and s1[j] == s2[i]:
                return True
            
        return len(diff_idx) == 0