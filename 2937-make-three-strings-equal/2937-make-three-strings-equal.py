class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        i = 0
        an, bn, cn = len(s1), len(s2), len(s3)
        while(i < min(an, bn, cn) and s1[i] == s2[i] == s3[i]):
            i += 1
        
        tot = (an - i) + (bn - i) + (cn - i)
        return -1 if(i == 0) else tot