class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if(start.replace('X', '') != end.replace('X', '')):
            return False
        
        ps = pe = 0
        sn, en = len(start), len(end)
        while(ps < sn and pe < en):
            s, e = start[ps], end[pe]
            if(s == e == 'L' and ps >= pe or \
               s == e == 'R' and ps <= pe):
                ps += 1
                pe += 1
                continue
            
            elif(s != 'X' and e != 'X'):
                return False
            
            else:
                ps += s == 'X'
                pe += e == 'X'
        
        return True