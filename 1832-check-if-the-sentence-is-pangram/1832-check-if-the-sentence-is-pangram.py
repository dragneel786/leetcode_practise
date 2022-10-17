class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        marker = [0] * 26
        count = 0
        for c in sentence:
            i = ord(c) - 97
            count += marker[i] == 0
            marker[i] = 1
            
            if(count == 26):
                return True
    
        return False