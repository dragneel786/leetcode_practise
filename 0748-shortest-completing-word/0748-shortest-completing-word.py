class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        letters = Counter([c.lower() for c in \
                           licensePlate if(c.isalpha())])
        
        res = None
        for word in words:
            if(not letters - Counter(word)\
               and (not res or len(word) < len(res))):
                res = word
        
        return res