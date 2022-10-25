class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        def char_by_char(words):
            for word in words:
                for char in word:
                    yield char
            yield None
        
        for a, b in zip(char_by_char(word1),\
                        char_by_char(word2)):
            if(a != b):
                return False
        
        return True