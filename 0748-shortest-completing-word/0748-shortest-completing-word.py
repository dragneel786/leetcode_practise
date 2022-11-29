class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        letters = Counter([c.lower() for c in \
                           licensePlate if(c.isalpha())])
        
        res = None
        words.sort(key=lambda x: len(x))
        for word in words:
            if(not letters - Counter(word)):
                return word