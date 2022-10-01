class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        scounts = Counter()
        gcounts = Counter()
        bull = cow = 0
        
        for s, g in zip(secret, guess):
            if(s == g):
                bull += 1
            else:
                scounts[s] += 1
                gcounts[g] += 1
        
        cow = scounts & gcounts
        
        return str(bull) + 'A' + str(sum(cow.values())) + 'B'
        