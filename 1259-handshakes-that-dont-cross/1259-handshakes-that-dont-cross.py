class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        
        @lru_cache(None)
        def total_ways(people_size):
            nonlocal MOD, numPeople            
            if(people_size % 2 == 1):
                return 0
            
            if(people_size == 0):
                return 1
            
            ways = 0
            for i in range(0, people_size, 2):
                ways += total_ways(i) * total_ways(people_size - i - 2)
                ways %= MOD
            
            return ways
    
        
        MOD = 10 ** 9 + 7
        return total_ways(numPeople)