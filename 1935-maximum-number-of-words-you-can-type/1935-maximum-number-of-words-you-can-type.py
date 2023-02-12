class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        char_set = [0] * 26
        for c in brokenLetters:
            char_set[ord(c) - 97] += 1
        
        complete = 0
        for word in text.split(" "):
            for c in word:
                if(char_set[ord(c) - 97]):
                    break
            else:
                complete += 1
                
        return complete