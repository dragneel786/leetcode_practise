class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        @lru_cache(None)
        def check_scramble(s1, s2):
            if(s1 == s2):
                return True
            
            n = len(s1)
            if(n <= 1):
                return False

            for i in range(1, n):
                if(check_scramble(s1[:i], s2[:i]) and
                   check_scramble(s1[i:], s2[i:])):
                    return True
                
                elif(check_scramble(s1[:i], s2[-i:]) and\
                     check_scramble(s1[i:], s2[:-i])):
                    return True
            return False
        
        
        return sorted(s1) == sorted(s2)\
    and check_scramble(s1, s2)