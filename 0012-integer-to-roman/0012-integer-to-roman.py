class Solution:
    def intToRoman(self, num: int) -> str:
        sym_val = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C',\
                   500:'D', 1000:'M', 4:'IV', 9:'IX',\
                   40:'XL', 90:'XC', 400:'CD', 900:'CM'}
        
        def get_symbol(place, val):
            if((val * place) in sym_val):
                return sym_val[(val * place)]
            
            temp = ''
            if(6 <= val <= 8):
                val -= 5
                temp += sym_val[(5 * place)]
        
            if(1 <= val <= 5):
                temp += (sym_val[place] * val)
                
            return temp
        
        
        num = str(num)
        n = len(num)
        res = ''
        for i in range(1, n + 1):
            place = 10 ** (n - i)
            val = int(num[i - 1])
            if(not val): continue
            res += get_symbol(place, val)
        
        return res