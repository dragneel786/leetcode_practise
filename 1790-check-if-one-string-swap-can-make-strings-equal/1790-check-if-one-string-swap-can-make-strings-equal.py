class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = 0
        counts = Counter()
        for a, b in zip(s1, s2):
            counts[a] += 1
            counts[b] -= 1
            diff += a != b
            if(diff > 2):
                return False
        
        return not any(counts.values())