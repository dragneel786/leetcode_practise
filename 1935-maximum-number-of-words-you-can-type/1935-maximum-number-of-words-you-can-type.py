class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        char_set = set(list(brokenLetters))
        complete = 0
        for word in text.split(" "):
            for c in word:
                if(c in char_set):
                    break
            else:
                complete += 1
                
        return complete