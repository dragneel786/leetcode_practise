class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sumation = []
        c = 0
        for a, b in zip_longest(a[::-1], b[::-1]):
            c += (a == '1') + (b == '1')
            sumation.append(str(c % 2))
            c //= 2
        
        if(c):
            sumation.append(str(c))
        return ''.join(sumation)[::-1]