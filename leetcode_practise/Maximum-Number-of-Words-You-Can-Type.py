class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        brokenLetters = set(brokenLetters)
        for word in text.split(" "):
            for c in word:
                if c in brokenLetters:
                    break
            else:
                res += 1
        
        return res
            
            

