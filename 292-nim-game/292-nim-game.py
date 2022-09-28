class Solution:
    def canWinNim(self, n: int) -> bool:
        return ((n >> 2) << 2) != n