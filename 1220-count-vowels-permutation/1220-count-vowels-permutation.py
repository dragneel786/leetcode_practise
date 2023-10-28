class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        options = {'a': ['e'], 'e':['a', 'i'],\
                   'i':['a', 'e', 'o', 'u'],\
                   'o':['i', 'u'], 'u':['a']}
        
        MOD = (10 ** 9) + 7
        
        @cache
        def counts(curr = '' , size = 0):
            nonlocal MOD
            if(size == n):
                return 1
            
            tot = 0
            op = ['a', 'e', 'i', 'o', 'u'] \
            if(curr not in options) else options[curr]
            
            for c in op:
                tot = (tot + counts(c, size + 1)) % MOD
            
            return tot
        
        return counts()
                