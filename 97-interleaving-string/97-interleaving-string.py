class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if(l1 + l2 != l3):
            return False
        
        @functools.lru_cache(None)
        def checkInter(i, j, k):
            nonlocal l1, l2, l3
            if(i == l1 and j == l2 and k == l3):
                return True
            
            res = False
            if(i < l1 and s1[i] == s3[k]):
                res |= checkInter(i + 1, j, k + 1)
            if(not res and j < l2 and s2[j] == s3[k]):
                res |= checkInter(i, j + 1, k + 1)
            return res
        
        return checkInter(0, 0, 0)
            
                