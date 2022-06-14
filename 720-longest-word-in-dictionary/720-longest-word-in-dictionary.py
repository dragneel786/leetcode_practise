class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = set(words)
        combo = [""]
        while(True):
            temp = []
            for c in combo:
                for i in range(26):
                    w = c + chr(i + 97)
                    if(w in words):
                        temp.append(w)
            if(not temp):
                break
            combo = temp[:]

        return combo[0]

                
        
                
        
        