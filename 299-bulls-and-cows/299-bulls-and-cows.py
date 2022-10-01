class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        ncount = [0] * 10
        bull = cow = 0
        
        for s, g in zip(secret, guess):
            if(s == g):
                bull += 1
            else:
                s, g = int(s), int(g)
                cow += int(ncount[s] > 0) + int(ncount[g] < 0)
                ncount[s] -= 1
                ncount[g] += 1
        
        return str(bull) + 'A' + str(cow) + 'B'
        