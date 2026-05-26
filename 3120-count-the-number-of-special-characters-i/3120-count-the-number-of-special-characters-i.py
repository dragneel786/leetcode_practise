class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_case = Counter()
        counts = 0
        for c in word: 
            if 'a' <= c <= 'z':
                lower_case[c] += 1
            
        for c in word:
            if c.isupper() and lower_case[c.lower()] > 0:
                lower_case[c.lower()] = 0
                counts += 1
        
        return counts

                