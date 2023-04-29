class Solution:
    def pivotInteger(self, n: int) -> int:
        tot = (n * (n + 1)) // 2
        sumi = 0
        for i in range(1, n + 1):
            sumi += i
            if(sumi == (tot - sumi + i)):
                return i
        
        return -1