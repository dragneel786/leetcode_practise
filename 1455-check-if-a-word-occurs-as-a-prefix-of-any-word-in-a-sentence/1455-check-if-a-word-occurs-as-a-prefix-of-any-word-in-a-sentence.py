class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        size = len(searchWord)
        for i, word in enumerate(sentence.split()):
            if word[:size] == searchWord:
                return i + 1
        
        return -1