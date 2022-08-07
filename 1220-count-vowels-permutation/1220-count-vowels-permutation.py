class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        paths = {'$':['a', 'e', 'i', 'o', 'u'], 'a':['e'], 'e':['a', 'i'],\
                 'i':['a', 'e', 'o', 'u'], 'o':['u', 'i'], 'u':['a']}
        
        M = (10 ** 9) + 7
        
        def getStringCounts(l, op = '$', memo = {}):
            if(not l): return 1
            
            key = (l, op[-1])
            if(key in memo):
                return memo[key]
            
            counts = 0
            for c in paths[op[-1]]:
                counts = (counts + getStringCounts(l - 1, op + c)) % M
            
            memo[key] = counts
            return counts
        
        return getStringCounts(n)
        
            