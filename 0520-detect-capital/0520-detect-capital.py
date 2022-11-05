class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if(n == 1): return True
        
        word += word[-1]
        upper = True
        for i in range(1, n):
            up = word[i].isupper()
            if(up != word[i + 1].isupper()):
                return False
            
            upper &= up
        
        fup = word[0].isupper()
        return fup if(upper) else True
    
        
        
    
        
        
        
        