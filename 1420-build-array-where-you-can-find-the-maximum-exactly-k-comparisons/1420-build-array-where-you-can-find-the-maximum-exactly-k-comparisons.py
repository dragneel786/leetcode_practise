class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        
        @lru_cache(None)
        def find_ways(idx, len_lis, large):
            nonlocal MOD
            if(len_lis > k):
                return 0
            
            if(idx == n):
                return len_lis == k
            
            ways = 0
            for i in range(1, m + 1):
                if(i <= large):
                    ways += find_ways(idx + 1, len_lis, large)
                else:
                    ways += find_ways(idx + 1, len_lis + 1, i)
            
            return ways % MOD
        
        MOD = (10 ** 9) + 7
        return find_ways(0, 0, -1) % MOD