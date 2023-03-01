class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        for i in range(n):
            wn = len(words[i])
            if(n < wn):
                return False
            words[i] += ('-' * (n - wn)) 
            
        for k in range(n):
            for r in range(k + 1):
                c = n - k - 1 + r
                if(words[r][c] != words[c][r]):
                    return False
        
        return True
                
            
           