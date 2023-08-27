class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * height * width
        if(any(x > 9999 for x in (length, width, height))\
           or volume > (10 ** 9 - 1)):
            return 'Bulky' if(mass < 100) else 'Both'
        
        if(mass > 99):
            return 'Heavy'
        
        return "Neither"
        
        