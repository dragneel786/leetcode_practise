class Solution:
    def generateTag(self, caption: str) -> str:
        res = ['#']
        for i, word in enumerate(map(lambda w: w.lower(),\
         caption.split())):
            if len(word):
                ch = word[0]
                if i != 0:
                    ch = ch.upper()
                
                res.append(ch + word[1:])
        
        return ''.join(res)[:100]

