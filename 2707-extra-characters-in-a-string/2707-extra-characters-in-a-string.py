class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        min_del = [inf] * (n + 1)
        min_del[-1] = 0
        dictionary = set(dictionary)
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i:j + 1] in dictionary:
                    min_del[i] = min(min_del[i], min_del[j + 1])
                
                else:
                    min_del[i] = min(min_del[i], min_del[j + 1] + (j - i + 1))
        
        return min_del[0]
            
        
        