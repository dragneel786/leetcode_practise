class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if(word1 == word2):
            prev = -inf
            mind = inf
            for i, w in enumerate(wordsDict):
                if(w == word1):
                    mind = min(mind, i - prev)
                    prev = i
            return mind
        
        n = len(wordsDict)
        prevl = inf
        prevr = inf
        lindex = [inf] * n
        rindex = [inf] * n
        for i in range(n):
            if(word1 == wordsDict[i]):
                prevl = i
            lindex[i] = prevl
            
            if(word1 == wordsDict[n - i - 1]):
                prevr = n - i - 1
            rindex[n - i - 1] = prevr
        
        
        ans = inf
        for i in range(n):
            if(word2 == wordsDict[i]):
                ans = min(ans, abs(i - lindex[i]),\
                          abs(i - rindex[i]))
        
        return ans
        
        
        
        
        
        