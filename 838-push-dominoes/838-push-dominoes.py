class Solution:
    def pushDominoes(self, d: str) -> str:
        d = 'L' + d + 'R'
        i = 0
        ans = ''
        for j in range(1, len(d)):
            if(d[j] == '.'): continue
            
            between_size = j - i - 1
            if(i):
                ans += d[i]
                
            if(d[i] == d[j]):
                ans += d[i] * between_size
                
            elif(d[i] == 'L' and d[j] == 'R'):
                ans += '.' * between_size
                
            else:
                half = between_size // 2
                ans += 'R' * half + '.' * (between_size & 1) +\
                'L' * half
            
            i = j
        
        return ans
                
                
                
        
        