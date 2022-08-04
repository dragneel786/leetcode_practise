class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while(not p % 2 and not q % 2): p, q = p >> 1, q >> 1
        return 1 - p % 2 + q % 2