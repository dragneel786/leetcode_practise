class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @lru_cache(None)
        def convert_dis(i = 0, j = 0):
            nonlocal n1, n2
            if(j == n2):
                return n1 - i
            
            if(i == n1):
                return n2 - j
            
            
            if(word1[i] != word2[j]):
                delete = convert_dis(i + 1, j)
                insert = convert_dis(i, j + 1)
                replace = convert_dis(i + 1, j + 1)
                return min(delete, insert, replace) + 1
            else:
                return convert_dis(i + 1, j + 1)
            
            
        
        n1, n2 = len(word1), len(word2)
        return convert_dis()