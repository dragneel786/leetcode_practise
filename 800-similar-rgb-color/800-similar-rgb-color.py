class Solution:
    def similarRGB(self, color: str) -> str:
        
        convert_sq = lambda a, b: (int(a, 16) - int(b, 16)) ** 2
        similarity = lambda x, y: - convert_sq(x[:2], y[:2])\
        - convert_sq(x[2:4], y[2:4]) - convert_sq(x[4:], y[4:])
        
        
        hexi = '0123456789abcdef'
        similar, res = -inf, ""
        for combo in itertools.product(hexi, repeat=3):
            combo_hex = combo[0] * 2 + combo[1] * 2 + combo[2] * 2
            temp_similar = similarity(color[1:], combo_hex)
            
            if(temp_similar > similar):
                res = '#' + combo_hex
                similar = temp_similar
                
        return res