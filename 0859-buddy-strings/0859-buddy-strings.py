class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        m, n = len(s), len(goal)
        if(m != n):
            return False
        
        a, x = '1', '1'
        b, y = '0', '0'
        counts = Counter()
        for c, d in zip(s, goal):
            if(c == d):
                counts[c] += 1
                continue
                
            if(a == '1'):
                a, x = c, d
            
            elif(b == '0'):
                y, b = c, d
            
            else:
                return False
        
        if(a != '1'):
            return (a == b and x == y)
        
        return len(list(filter(lambda v:v>=2, counts.values())))
                
                