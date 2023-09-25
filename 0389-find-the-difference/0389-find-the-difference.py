class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor = 0
        for a, b in zip_longest(s, t):
            if(a):
                xor ^= ord(a)
            xor ^= ord(b)
        
        return chr(xor)