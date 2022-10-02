class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        n = len(wordsDict)
        word1_idx = [inf] * n
        min_dis = back = front = inf
        
        for i in range(n):
            if(wordsDict[i] == word1):
                front = i
            else:
                word1_idx[i] = min(abs(front - i), word1_idx[i])
            
            if(wordsDict[n - i - 1] == word1):
                back = n - i - 1
            else:
                word1_idx[n - i - 1] = min(word1_idx[n - i - 1],\
                                           abs(back - (n - i - 1)))
        
        for i, w in enumerate(wordsDict):
            if(w == word2):
                min_dis = min(min_dis, word1_idx[i])
          
        return min_dis
        
        