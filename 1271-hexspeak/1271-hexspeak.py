class Solution:
    def toHexspeak(self, num: str) -> str:
        n = int(num)
        hx = list((hex(n)[2:]).upper())
        hexis = {'A', 'B', 'C', 'D', 'E', 'F'}
        print(hx)
        for i, c in enumerate(hx):
            if(c == '0'):
                hx[i] = 'O'
            elif(c == '1'):
                hx[i] = 'I'
            elif(c not in hexis):
                return "ERROR"
            
        return ''.join(hx)
            