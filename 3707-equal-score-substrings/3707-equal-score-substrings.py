class Solution:
    def scoreBalance(self, s: str) -> bool:
        tot = 0
        for c in s:
            tot += ord(c) - 96
        
        second = 0
        for c in s:
            val = ord(c) - 96
            second += val
            tot -= val
            if tot == second:
                return True
        
        return False