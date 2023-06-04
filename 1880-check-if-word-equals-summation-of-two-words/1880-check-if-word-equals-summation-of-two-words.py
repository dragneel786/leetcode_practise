class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def int_(word):
            num = 0
            for c in word:
                num = (num * 10) + (ord(c) - 97)
            return num
        
        a, b, c = int_(firstWord), int_(secondWord), int_(targetWord)
        return a + b == c