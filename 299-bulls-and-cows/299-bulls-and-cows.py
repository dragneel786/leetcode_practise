class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s = Counter(secret)
        g = Counter(guess)
        bulls = 0
        cows = 0
        for k in g.keys():
            cows += min(s[k], g[k]) if(k in s) else 0
        
        for i in range(len(guess)):
            if(secret[i] == guess[i]):
                bulls += 1
        
        return str(bulls) + "A" + str(cows - bulls) + "B"
        