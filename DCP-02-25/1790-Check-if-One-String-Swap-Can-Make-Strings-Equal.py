class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff1 = []
        diff2 = []
        for i, (a, b) in enumerate(zip(s1, s2)):
            if a != b:
                diff1.append(a)
                diff2.append(b)
        
        return len(diff1) in [0, 2] and len(diff2) in [0, 2] and sorted(diff1) == sorted(diff2)
            
