class Solution:
    def knightDialer(self, n: int) -> int:
        kmap = {0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9],\
                5:[], 6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4]}
        MOD = (10 ** 9) + 7
        
        
        @lru_cache(None)
        def find_combos(n, curr):
            if(not n):
                return 1
            
            counts = 0
            for pad in kmap[curr]:
                counts = (counts + find_combos(n - 1, pad)) % MOD
            
            return counts
        
        
        ans = 0
        for key in kmap.keys():
            ans = (ans + find_combos(n - 1, key)) % MOD
        
        return ans
        
            
        