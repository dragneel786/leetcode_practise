class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        s1 = set([1, 8, 0, 2, 5, 6, 9])
        s2 = set([1, 8, 0])
        s = set()
        N = list(map(int, str(n)))
        res = 0
        for i, v in enumerate(N):
            for j in range(v):
                if(s.issubset(s1) and j in s1):
                    res += 7 ** (len(N) - i - 1)
                if(s.issubset(s2) and j in s2):
                    res -= 3 ** (len(N) - i - 1)
            
            if(v not in s1):
                return res
        
            s.add(v)
        
        return res + (s.issubset(s1) and not s.issubset(s2))