class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if(len(word) == 1):
            return True
        
        def upper_lower():
            lower = upper = False
            for c in word[1:]:
                lower |= c.islower()
                upper |= c.isupper()
            return lower, upper
        
        
        first_lower = word[0].islower()
        lo, up = upper_lower()
        return (lo != up) and ((first_lower and lo) or (not first_lower and (lo or up)))