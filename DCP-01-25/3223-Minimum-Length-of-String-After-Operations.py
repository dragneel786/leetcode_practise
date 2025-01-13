class Solution:
    def minimumLength(self, s: str) -> int:
        counts = [0] * 26
        for c in s:
            idx = ord(c) - 97
            counts[idx] += 1
            if counts[idx] >= 3:
                counts[idx] -= 2
        
        return sum(counts)


