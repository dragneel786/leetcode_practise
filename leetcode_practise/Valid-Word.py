class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        if not word.isalnum():
            return False
        
        vowels = "aeiou"
        vowel = False
        conso = False
        for c in word:
            if c.lower() in vowels:
                vowel = True
            
            if(c.isalpha() and c.lower() not in vowels):
                conso = True
            
            if vowel and conso:
                return True
        
        return False