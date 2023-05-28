class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        @lru_cache(None)
        def min_cost(start, end, size):
            nonlocal n
            if(start >= end):
                return 0
            
            ans = inf
            left = 0 if(start == 0) else cuts[start - 1]
            right = n if(end == len(cuts)) else cuts[end]
            cost = right - left
            
            for i in range(start, end):
                lcut = min_cost(start, i, left)
                rcut = min_cost(i + 1, end, right)
                ans = min(ans, lcut + rcut + cost)
            
            return ans
                
        cuts.sort()
        return min_cost(0, len(cuts), n)