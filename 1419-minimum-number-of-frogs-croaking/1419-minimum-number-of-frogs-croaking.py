class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cmap = {'c':'#', 'r':'c', 'o':'r',\
                'a':'o', 'k':'a'}
        
        frogs = 0
        countMap = Counter({'#': inf})
        for c in croakOfFrogs:
            if(countMap[cmap[c]] > countMap[c]):
                countMap[c] += 1
            else:
                return -1
            
            if(c == 'k'):
                frogs = max(countMap['c'], frogs)
                for ch in 'croak':
                    countMap[ch] -= countMap['k']
            
        return -1 if(countMap['c']) else frogs