class Solution:
    def convertToBase7(self, num: int) -> str:
        if(num == 0):
            return '0'
        sym = (num < 0)
        num = abs(num)
        res = []
        while(num >= 7):
            res.append(num % 7)
            num //= 7
        
        if(num):
            res.append(num)
        
        return ('-' * sym) + ''.join(map(str, reversed(res)))