class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_dict = DefaultDict(int)
        upper_dict = DefaultDict(int)
        for i, c in enumerate(word):
            if c.islower():
                lower_dict[c] = i
            
            if c.isupper() and c not in upper_dict:
                upper_dict[c] = i
        
        counts = 0
        for k, v in lower_dict.items():
            if upper_dict[k.upper()] > v:
                counts += 1
        
        return counts
            