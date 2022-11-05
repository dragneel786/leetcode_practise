class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if(n == 1): return True
        
        word += word[-1]
        upper = True
        for i in range(1, n):
            if(word[i].islower() !=\
               word[i + 1].islower()):
                return False
            
            upper &= word[i].isupper()
        
        fup = word[0].isupper()
        return fup if(upper) else True
    
        
        
    
        
        
        
        