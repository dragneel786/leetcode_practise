class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs, ct = Counter(s), Counter(t)
        s1 = sum((cs - ct).values())
        s2 = sum((ct - cs).values())
        return s1 + s2