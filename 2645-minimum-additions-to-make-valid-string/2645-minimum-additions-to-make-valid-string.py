class Solution:
    def addMinimum(self, word: str) -> int:
        
        # acbabac
        # a, b, c
        key = "abc"
        i = insert = 0
        for c in word:
            while(c != key[i]):
                i = (i + 1) % 3
                insert += 1
            
            i = (i + 1) % 3
        
        return insert + ((3 - i) if i > 0 else 0)
            