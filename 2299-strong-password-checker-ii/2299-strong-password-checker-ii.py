class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        lcase = ucase = digit = special = False
        if(len(password) < 8):
            return False
        
        for i,c in enumerate(password):
            lcase = lcase or c.islower()
            ucase = ucase or c.isupper()
            digit = digit or c.isdigit()
            special = special or c in "!@#$%^&*()-+"
            if(i > 0 and c == password[i - 1]):
                return False
        
        return all([lcase, ucase, digit, special])
                
            