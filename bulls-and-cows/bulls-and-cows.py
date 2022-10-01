class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        scounts = Counter(secret)
        gcounts = Counter(guess)
        bull = cow = 0
        
        for s, g in zip(secret, guess):
            if(s == g):
                bull += 1
                scounts[s] -= 1
                gcounts[g] -= 1
                if(not gcounts[g]): del gcounts[g]
                if(not scounts[s]): del scounts[s]
        
        for g, v in gcounts.items():
            if(scounts[g]):
                cow += min(scounts[g], v)
        
        return str(bull) + 'A' + str(cow) + 'B'
        