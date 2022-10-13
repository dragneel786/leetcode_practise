class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split()
        if(len(pattern) != len(slist)):
            return False
        
        imap = dict()
        for i, (p, w) in enumerate(zip(pattern, slist)):
            idx1 = imap.setdefault(f'char_{p}', i)
            idx2 = imap.setdefault(f'word_{w}', i)
            if(idx1 != idx2):
                return False
        
        return True