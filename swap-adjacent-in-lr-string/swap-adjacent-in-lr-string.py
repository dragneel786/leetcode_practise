class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if(start.replace('X', '') != end.replace('X', '')):
            return False
        
        ps = pe = 0
        sn, en = len(start), len(end)
        while(ps < sn and pe < en):
            if(start[ps] != 'X' and end[pe] != 'X'):
                if(start[ps] == 'L' and ps < pe):
                    return False

                if(start[ps] == 'R' and ps > pe):
                    return False
                ps, pe = ps + 1, pe + 1
                continue
            
            ps += start[ps] == 'X'
            pe += end[pe] == 'X'
        
        return True