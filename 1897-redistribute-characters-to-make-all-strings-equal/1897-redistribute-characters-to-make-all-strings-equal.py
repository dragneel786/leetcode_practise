class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        tot = [0] * 26
        for word in words:
            for w in word:
                idx = ord(w) - 97
                tot[idx] += 1
        
        n = len(words)
        for v in tot:
            if(v % n != 0):
                return False
        
        return True