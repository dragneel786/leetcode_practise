class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if(start.replace('X', '') != end.replace('X', '')):
            return False
        
        ps = pe = 0
        sn, en = len(start), len(end)
        while(ps < sn and pe < en):
            if(start[ps] == 'X' or end[pe] == 'X'):
                ps += start[ps] == 'X'
                pe += end[pe] == 'X'
            
            else:
                if(start[ps] == 'L' and ps < pe):
                    return False

                if(start[ps] == 'R' and ps > pe):
                    return False
            
                ps += 1
                pe += 1
        
        return (ps == sn or pe == en)