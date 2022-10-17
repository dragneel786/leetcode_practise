class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count = 0
        for c in sentence:
            count |= 1 << (ord(c)- 97)
            if(count + 1 == 1 << 26):
                return True
            
        return False