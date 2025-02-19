class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        def pset(size, chars):
            nonlocal res
            if size == 0:
                res.append(''.join(chars))
                return
            
            for c in ['a', 'b', 'c']:
                if len(chars) == 0 or chars[-1] != c:
                    pset(size - 1, chars + [c])
            
        
        res = []
        pset(n, [])
        res.sort()
        return res[k - 1] if(len(res) >= k) else ""
        
