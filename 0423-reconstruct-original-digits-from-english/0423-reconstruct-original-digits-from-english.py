class Solution:
    def originalDigits(self, s: str) -> str:
        nc = Counter(s)
        c = Counter()
        # zero, one, two, three, four, five, six, seven, eight, nine
        c['0'] = nc['z']
        c['2'] = nc['w']
        c['4'] = nc['u']
        c['6'] = nc['x']
        c['8'] = nc['g']
    
        c['3'] = nc['h'] - c['8']
        c['5'] = nc['f'] - c['4']
        c['7'] = nc['s'] - c['6']
    
        c['9'] = nc['i'] - c['5'] - c['6'] - c['8']
        c['1'] = nc['n'] - c['7'] - (c['9'] * 2)
        
        res = ''
        for k in '0123456789':
            print(c[k])
            res += (k * c[k])
        
        return res
            
        