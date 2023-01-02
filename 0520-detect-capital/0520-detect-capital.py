class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_upper = True
        all_lower = True
        first_char = word[0].isupper()
        for c in word[1:]:
            all_upper = all_upper and c.isupper()
            all_lower = all_lower and c.islower()
            
        
        return (first_char and (all_upper or all_lower)) or all_lower
            
            
        