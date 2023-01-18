class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = 0
        for c in s:
            pos = 1 << (ord(c) - 97)
            if(seen & pos):
                return c
            seen |= pos