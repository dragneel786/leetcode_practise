class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        splits = s.split()
        if(len(splits) != len(pattern)):
            return False
        
        pmap = dict()
        for a, b in zip(pattern, s.split()):
            if(pmap.get('1' + a, None) not in [b, None]\
               or pmap.get('2' + b, None) not in [a, None]):
                return False
            pmap['1' + a] = b
            pmap['2' + b] = a
        
        return True