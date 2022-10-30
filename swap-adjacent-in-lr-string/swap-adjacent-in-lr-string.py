class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if(start.replace('X', '') != end.replace('X', '')):
            return False
        
        ps = pe = 0
        sn, en = len(start), len(end)
        while(ps < sn and pe < en):
            while(ps < sn and start[ps] == 'X'):
                ps += 1
            
            while(pe < en and end[pe] == 'X'):
                pe += 1
            
            if(ps == sn and pe == en):
                return True
            
            if(ps == sn or pe == en):
                return False
            
            s, e = start[ps], end[pe]
            if(s != e):
                return False
            
            if(s == 'L' and ps < pe):
                return False
            
            if(s == 'R' and ps > pe):
                return False
            
            ps += 1
            pe += 1
        
        return True