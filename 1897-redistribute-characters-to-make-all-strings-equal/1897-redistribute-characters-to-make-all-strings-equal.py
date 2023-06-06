class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        fcounts = Counter()
        for w in words:
            fcounts += Counter(w)
        
        for k, v in fcounts.items():
            if(v % n):
                return False
        
        return True
        