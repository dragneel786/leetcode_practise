class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = 0
        imap = [0] * 26
        for a, b in zip(s1, s2):
            imap[ord(a) - 97] += 1
            imap[ord(b) - 97] -= 1
            diff += a != b
        
        return diff < 3 and not any(imap)