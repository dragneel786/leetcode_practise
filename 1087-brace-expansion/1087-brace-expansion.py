class Solution:
    def expand(self, s: str) -> List[str]:
        
        def get_options(s, i):
            j = i + 1
            while(s[j] != '}'): j += 1
            return (s[i + 1: j]).split(","), j
        
        def allCombos(start, op = ""):
            nonlocal n, res
            if(start == n): 
                res.append(op)
                return
            
            if(s[start] == '{'):
                options, idx = get_options(s, start)
                for option in options:
                    allCombos(idx + 1, op + option)
            else:
                allCombos(start + 1, op + s[start])
        
        n = len(s)
        res = []
        allCombos(0)
        return sorted(res)
        
        
            