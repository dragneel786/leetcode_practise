class Solution:
    def similarRGB(self, color: str) -> str:
        min_val = lambda val: min('0123456789abcdef',\
                  key=lambda x: abs(int(x*2, 16) - int(val, 16)))
        
        
        return '#' + ''.join([min_val(color[i:i + 2])\
                              for i in range(1, 7, 2)])
        