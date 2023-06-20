class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        black = True
        ch = 'a'
        while(ch != coordinates[0]):
            black = not black
            ch = chr(ord(ch) + 1)
        
        num = 1
        while(num != int(coordinates[1])):
            num += 1
            black = not black
        
        return not black