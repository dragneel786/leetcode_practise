class Solution:
    def reorganizeString(self, s: str) -> str:
        
        def finder():
            max_val = 0
            found = ''
            for c in counts:
                if(c != prev and max_val < counts[c]):
                    found = c
                    max_val = counts[c]
                    
            return found
                    
        counts = Counter(s)
        prev = ''
        res = ''
        for _ in range(len(s)):
            ch = finder()
            if(not ch):
                return ''
            
            res += ch
            prev = ch
            counts[ch] -= 1
        
        return res
            
        