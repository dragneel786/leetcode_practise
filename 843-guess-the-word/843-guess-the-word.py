# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def helper(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))
        
        def getPowerWord():
            wordCount = [([0] * 26) for _ in range(6)]
            for w in wordlist:
                for i in range(6):
                    wordCount[i][ord(w[i]) - 97] += 1
                    
            word = (0, "")
            for w in wordlist:
                s = 0
                for i in range(6):
                    s += wordCount[i][ord(w[i]) - 97]
                if(s > word[0]):
                    word = (s, w)
            return word[1]

        while(wordlist):
            w = getPowerWord()
            l = master.guess(w)
            if(l == 6):
                return
            wordlist = [x for x in wordlist if(helper(x, w) == l)]
            
        
            