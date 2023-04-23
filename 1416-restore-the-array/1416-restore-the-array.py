class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        
        @lru_cache(None)
        def total_ways(idx):
            nonlocal k, n, s
            if(idx >= n):
                return 1
            
            if(s[idx] == '0'):
                return 0
            
            count = 0
            num = []
            for i in range(idx, n):
                num.append(s[i])
                if(int(''.join(num)) > k):
                    return count
                
                count = (count + total_ways(i + 1)) % MOD
            
            return count % MOD
        
        MOD = 10 ** 9 + 7
        n = len(s)
        return total_ways(0)