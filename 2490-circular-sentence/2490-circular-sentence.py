class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        splits = sentence.split(" ")
        for i in range(1, len(splits)):
            if(splits[i - 1][-1] != splits[i][0]):
                return False
        
        return splits[0][0] == splits[-1][-1]