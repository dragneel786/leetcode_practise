class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cmap = {'c':'#', 'r':'c', 'o':'r',\
                'a':'o', 'k':'a'}
        
        frogs = 0
        countMap = Counter({'#': inf})
        for c in croakOfFrogs:
            prevc = cmap[c]
            countMap[c] += 1
        
            if(countMap[prevc] < countMap[c]):
                return -1
            
            if(c == 'k'):
                for ch in 'croak':
                    frogs = max(countMap[ch], frogs)
                    countMap[ch] -= countMap['k']
            
        return -1 if(countMap['c'] != countMap['k']) else frogs