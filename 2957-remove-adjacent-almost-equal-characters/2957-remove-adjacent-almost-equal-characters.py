class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        if len(word) < 2:
            return 0

        ops, i = 0, 1
        while i < len(word):
            if word[i] == chr(ord(word[i - 1]) + 1) or\
            word[i] == chr(ord(word[i - 1]) - 1) or\
            word[i] == word[i - 1]:
                ops += 1
                i += 2
            
            else:
                i += 1
            
        return ops